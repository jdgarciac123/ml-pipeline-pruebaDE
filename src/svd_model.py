import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds

def train_svd(df_svd):
    ratings = df_svd.drop(columns=["user_id"]).to_numpy()
    user_ids = df_svd["user_id"].values

    user_ratings_mean = np.mean(ratings, axis=1)
    R_demeaned = ratings - user_ratings_mean.reshape(-1, 1)

    k = min(ratings.shape) - 1
    U, sigma, Vt = svds(R_demeaned, k=k)
    sigma = np.diag(sigma)

    R_pred = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

    cols = df_svd.drop(columns=["user_id"]).columns
    pred_df = pd.DataFrame(R_pred, columns=cols, index=user_ids)

    return pred_df