import pandas as pd

def get_recommendations(pred_df, user_id, num_recommendations=5):
    user_preds = pred_df.loc[user_id].sort_values(ascending=False)
    top_items = user_preds.head(num_recommendations).index.tolist()
    top_scores = user_preds.head(num_recommendations).values.tolist()
    return top_items, top_scores

def build_recommendations(pred_df, user_ids, num_recommendations=5):
    recs = []
    for uid in user_ids:
        items, scores = get_recommendations(pred_df, uid, num_recommendations)
        row = {"user_id": uid}
        for i in range(num_recommendations):
            row[f"top_{i+1}"] = items[i]
            row[f"score_{i+1}"] = scores[i]
        recs.append(row)
    return pd.DataFrame(recs)