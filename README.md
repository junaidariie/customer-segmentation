# 🚀 Customer Segmentation API

🌐 **Live Frontend Demo:**
👉 [https://junaidariie.github.io/junaid17-customer-segmentation/](https://junaidariie.github.io/junaid17-customer-segmentation/)

> ⚡ **Note:** The frontend UI for this project is **AI-generated** and serves as a clean, interactive interface for demonstrating the backend capabilities. The core focus of this project is the **machine learning pipeline, API design, and deployment architecture**.

---

## 📌 Project Overview

This project is an **end-to-end customer segmentation system** built using **Machine Learning + FastAPI**.
It segments customers into meaningful groups based on behavioral and demographic attributes, enabling data-driven marketing and personalization strategies.

The system exposes a REST API that accepts customer data and returns:

* Customer segment classification
* Segment description
* Actionable business recommendations

---

## 🧠 Model Overview

* **Algorithm**: K-Means Clustering
* **Preprocessing**: Feature scaling using `StandardScaler`
* **Inference**: Cluster prediction with interpretation logic
* **Deployment**: FastAPI + Docker (Hugging Face compatible)

---

## 📊 Customer Segments

| Cluster | Segment Name                         | Description                                             |
| ------- | ------------------------------------ | ------------------------------------------------------- |
| 0       | High-Value Loyal Shoppers            | High income, high spending, frequent in-store purchases |
| 1       | Budget-Conscious Occasional Shoppers | Low spenders with recent engagement                     |
| 2       | Mid-Tier Engaged Browsers            | Frequent visitors with low recent spending              |
| 3       | Active Online-Focused Shoppers       | High-value users active across digital channels         |

Each prediction returns:

* `cluster_id`
* `cluster_name`
* `description`
* `recommendation`

---

## 📁 Project Structure

```
customer-segmentation-api/
│
├── artifacts/
│   ├── kmeans.pkl
│   └── scaler.pkl
│
├── data/
│   └── (dataset files)
│
├── app.py                  # FastAPI application
├── predict_helper.py       # ML inference logic
├── analysis_model.ipynb    # Model training & EDA
├── index.html              # AI-generated frontend
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Scikit-learn**
* **Pandas**
* **Joblib**
* **Uvicorn**
* **Docker**
* **Hugging Face Spaces**

---

## 🚀 API Endpoints

### 🔹 Health Check

```http
GET /
```

**Response**

```json
{
  "message": "The api server is live and working"
}
```

---

### 🔹 Predict Customer Segment

```http
POST /predict
```

#### Request Body

```json
{
  "Age": 35,
  "Income": 65000,
  "Total_Spendings": 1200,
  "NumWebPurchases": 8,
  "NumStorePurchases": 5,
  "NumWebVisitsMonth": 12,
  "Recency": 30
}
```

#### Response

```json
{
  "cluster_id": 3,
  "cluster_name": "Active Online-Focused Shoppers",
  "description": "High income, high spending, shops frequently both online and in-store.",
  "recommendation": "Offer premium bundles and omnichannel loyalty rewards."
}
```

---

## 🧩 Core Logic Flow

1. Request validation via **Pydantic**
2. Feature scaling using trained scaler
3. Cluster prediction via KMeans
4. Mapping cluster → business insight
5. Structured API response

---

## 🧪 Run Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the API

```bash
uvicorn app:app --reload
```

### 3️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Deployment

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
```

---

## 🌍 Deployment Options

* Hugging Face Spaces (Docker)
* AWS / GCP / Azure
* Local Docker environment

---

## ✨ Key Highlights

✔ End-to-end ML pipeline
✔ Clean FastAPI architecture
✔ AI-generated frontend
✔ Business-ready insights
✔ Production-deployable

---

## 🔮 Future Enhancements

* Confidence scoring per prediction
* Model explainability (SHAP / feature importance)
* User analytics dashboard
* Role-based access control

---

## 👨‍💻 Author

**Junaid**
AI / Machine Learning Engineer
Focused on production-grade ML systems, risk modeling, and real-world AI deployment.

---
