import pandas as pd

def load_data(path_prints, path_taps, path_pays):
    df_prints = pd.read_json(path_prints, lines=True)
    df_prints = df_prints.join(pd.json_normalize(df_prints["event_data"]))
    df_prints["day"] = pd.to_datetime(df_prints["day"])

    df_taps = pd.read_json(path_taps, lines=True)
    df_taps = df_taps.join(pd.json_normalize(df_taps["event_data"]))
    df_taps["day"] = pd.to_datetime(df_taps["day"])

    df_pays = pd.read_csv(path_pays)
    df_pays = df_pays.rename(columns={"pay_date": "day"})
    df_pays["day"] = pd.to_datetime(df_pays["day"])

    return df_prints, df_taps, df_pays