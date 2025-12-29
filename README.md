[Live Demo (dummy)](https://example.com/customer-segmentation-demo)

# Customer Segmentation

Simple customer segmentation project using KMeans to cluster retail customers and provide targeted recommendations.

## Overview
- Trains a KMeans model on customer features and exposes a FastAPI endpoint for predictions.
- Includes EDA in `analysis_model.ipynb`, model artifacts in `artifacts/`, and an API in `app.py`.

## Features
- Preprocessing & feature engineering
- KMeans clustering with scaler persistence
- FastAPI service for real-time predictions

## Quick Start

Prerequisites: Python 3.8+ and `venv`.

1. Create and activate a virtual environment (Windows):

```powershell
python -m venv myenv
myenv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Ensure model artifacts exist:

- `artifacts/kmeans.pkl`
- `artifacts/scaler.pkl`

4. Run the API server:

```powershell
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## API

- `GET /` — health/status
- `POST /predict` — predict customer cluster

Example request body:

```json
{
  "Age": 45,
  "Income": 60000,
  "Total_Spendings": 900,
  "NumWebPurchases": 6,
  "NumStorePurchases": 8,
  "NumWebVisitsMonth": 5,
  "Recency": 40
}
```

Example curl:

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d @payload.json
```

## Files
- `app.py` - FastAPI application
- `predict_helper.py` - loads artifacts and maps clusters to descriptions
- `analysis_model.ipynb` - EDA and model training notebook
- `data/customer_segmentation.csv` - dataset

## Notes
- The demo link at the top is a placeholder.
- If you move the `artifacts/` folder, update paths in `predict_helper.py` accordingly.

## Contributing
Feel free to open issues or PRs to improve models, add tests, or extend the API.

## License
MIT
