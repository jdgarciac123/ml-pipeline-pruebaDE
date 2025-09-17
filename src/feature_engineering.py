import pandas as pd
import numpy as np

def build_features(df_prints, df_taps, df_pays):

    fecha_max = df_prints["day"].max()
    fecha_inicio = fecha_max - pd.Timedelta(days=7)

    # Prints

    df_prints_semana = (
        df_prints[(df_prints["day"] > fecha_inicio) & (df_prints["day"] <= fecha_max)]
            .sort_values("day", ascending=False)
            .drop_duplicates(["user_id", "value_prop"])
    )

    df_prints_sem3 = df_prints[df_prints["day"] < fecha_inicio]

    prints_grouped = (
    df_prints_sem3.groupby(["user_id", "value_prop"])
             .agg(prints_count=("value_prop", "count"))
             .reset_index()
    )

    # Taps

    df_taps_semana = df_taps[["day", "user_id", "value_prop"]].copy()
    df_taps_semana["clic"] = 1

    df_taps_sem3 = df_taps[df_taps["day"] < fecha_inicio]

    taps_grouped = (
        df_taps_sem3.groupby(["user_id", "value_prop"])
               .agg(taps_count=("value_prop", "count"))
               .reset_index()
    )

    # Pays

    df_pays_sem3 = df_pays[df_pays["day"] < fecha_inicio]

    pays_grouped = (
        df_pays_sem3.groupby(["user_id", "value_prop"])
               .agg(pays_count=("value_prop", "count"),
                    pays_total=("total", "sum"))
               .reset_index()
    )

    # Estructura final modelos

    df_final = (
        df_prints_semana.merge(df_taps_semana, on = ["day", "user_id", "value_prop"], how="left")
            .merge(prints_grouped, on=["user_id", "value_prop"], how="left")
            .merge(taps_grouped, on=["user_id", "value_prop"], how="left")
            .merge(pays_grouped, on=["user_id", "value_prop"], how="left")
            .drop(["event_data"], axis=1)
    )

    for column in df_final.columns[4:]:

        if column != "pays_total":
            df_final[column] = df_final[column].fillna(0).astype(int)
        else:
            df_final[column] = df_final[column].fillna(0)

    # Agregar rating
    
    df_mod3 = df_final.copy()

    df_mod3["rating"] = (
        0.5 * df_mod3["pays_total"].apply(lambda x: np.log1p(x)) +
        0.25 * df_mod3["pays_count"] +
        0.15 * df_mod3["taps_count"] +
        0.10 * df_mod3["prints_count"] 
    )

    # Pivot
    df_svd = df_mod3.pivot(index="user_id", columns="value_prop", values="rating").fillna(0)

    return df_svd, df_final