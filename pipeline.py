import pandas as pd
from src import config
from src.preprocess import load_data
from src.feature_engineering import build_features
from src.svd_model import train_svd
from src.recommend import build_recommendations

def main():
    # 1. Cargar datos
    df_prints, df_taps, df_pays = load_data(config.RAW_PRINTS, config.RAW_TAPS, config.RAW_PAYS)

    # 2. Feature engineering
    df_svd = build_features(df_prints, df_taps, df_pays)
    df_svd.to_csv(config.PROCESSED_SVD)
    df_svd = pd.read_csv(config.PROCESSED_SVD)

    # 3. Entrenar SVD
    pred_df = train_svd(df_svd)

    # 4. Recomendaciones
    recomendaciones_df = build_recommendations(pred_df, df_svd["user_id"].values, config.NUM_RECOMMENDATIONS)
    recomendaciones_df.to_csv(config.OUTPUT_RECS, index=False)

if __name__ == "__main__":
    main()