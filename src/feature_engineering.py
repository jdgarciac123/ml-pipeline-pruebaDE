import pandas as pd
import numpy as np

def build_features(df_prints, df_taps, df_pays):
    taps_grouped = (
        df_taps.groupby(["user_id", "value_prop"])
               .agg(taps_count=("value_prop", "count"))
               .reset_index()
    )

    pays_grouped = (
        df_pays.groupby(["user_id", "value_prop"])
               .agg(pays_count=("value_prop", "count"),
                    pays_total=("total", "sum"))
               .reset_index()
    )

    top2_count = (
        df_prints[df_prints["position"] <= 1]
        .groupby(["user_id", "value_prop"])
        .agg(top2_count=("value_prop", "count"))
        .reset_index()
    )

    # Usuarios únicos
    df_users = pd.concat([
        df_prints[["user_id"]],
        df_taps[["user_id"]],
        df_pays[["user_id"]]
    ], ignore_index=True).drop_duplicates()

    # Productos únicos
    recomend = df_prints[["value_prop"]].drop_duplicates()

    # Cruzar usuarios x productos
    df_mod3 = (
        df_users.merge(recomend, how="cross")
        .merge(taps_grouped, on=["user_id", "value_prop"], how="left")
        .merge(pays_grouped, on=["user_id", "value_prop"], how="left")
        .merge(top2_count, on=["user_id", "value_prop"], how="left")
        .fillna(0)
    )

    # Casting
    for col in df_mod3.columns:
        if "count" in col:
            df_mod3[col] = df_mod3[col].astype(int)

    # Rating con pesos
    df_mod3["rating"] = (
        0.5 * df_mod3["pays_total"].apply(lambda x: np.log1p(x)) +
        0.25 * df_mod3["pays_count"] +
        0.15 * df_mod3["taps_count"] +
        0.10 * df_mod3["top2_count"]
    )

    # Pivot
    df_svd = df_mod3.pivot(index="user_id", columns="value_prop", values="rating").fillna(0)

    return df_svd