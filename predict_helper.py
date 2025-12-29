import joblib
import pandas as pd


kmeans  = joblib.load('artifacts/kmeans.pkl')
scaler  = joblib.load('artifacts/scaler.pkl')

CLUSTER_INFO = {
    0: {
        "name": "High-Value Loyal Shoppers",
        "description": "High income, high total spending, prefers in-store shopping, moderately recent purchases.",
        "recommendation": "Offer exclusive in-store experiences, VIP loyalty tiers, early access to new collections, and personalized concierge service."
    },
    1: {
        "name": "Budget-Conscious Occasional Shoppers",
        "description": "Low income, low spending, high web browsing, but made a very recent purchase.",
        "recommendation": "Target with limited-time discounts, entry-level product bundles, and personalized email offers based on browsing history to encourage repeat purchases."
    },
    2: {
        "name": "Mid-Tier Engaged Browsers",
        "description": "Mid-range income, low spending despite frequent website visits; hasn’t purchased in a long time.",
        "recommendation": "Re-engage with cart abandonment reminders, free shipping thresholds, or 'we miss you' incentives (e.g., 15% off). Highlight bestsellers and social proof to drive conversion."
    },
    3: {
        "name": "Active Online-Focused Shoppers",
        "description": "High income, high spending, shops frequently both online and in-store—with strongest activity on web.",
        "recommendation": "Offer premium bundles, omnichannel loyalty rewards (e.g., buy online, pick up in-store + bonus points), and personalized cross-channel recommendations."
    }
}

def predict(age, income, total_spending, num_web_purchases, num_store_purchases, num_web_visits, recency):
    input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Total_Spendings": [total_spending],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency]})

    scaled_data = scaler.transform(input_data)
    cluster_id = kmeans.predict(scaled_data)[0]

    info = CLUSTER_INFO[cluster_id]
    return {
        "cluster_id": int(cluster_id),
        "cluster_name": info["name"],
        "description": info["description"],
        "recommendation": info["recommendation"]
    }
    


"""if __name__ == "__main__":
    result = predict(45, 60000, 900, 6, 8, 5, 40)
    print(f"✨ Customer Segment: {result['cluster_name']} (ID: {result['cluster_id']})")
    print(f"📝 Profile: {result['description']}")
    print(f"🎯 Marketing Action: {result['recommendation']}")"""
