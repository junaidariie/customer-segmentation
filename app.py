from fastapi import FastAPI, HTTPException
from predict_helper import predict
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Customer Segmentation', version='1.0')

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class BaseInput(BaseModel):
    Age                 :   int = Field(..., ge=18, le=100, description="Customer age between 18 and 100")
    Income              :   int = Field(..., ge=0, le=200000, description="Income between 0 and 200000")
    Total_Spendings     :   int = Field(..., ge=0, le=5000, description="Total spendings (sum of purchases)")
    NumWebPurchases     :   int = Field(..., ge=0, le=100, description="Number of web purchases")
    NumStorePurchases   :   int = Field(..., ge=0, le=100, description="Number of store purchases")
    NumWebVisitsMonth   :   int = Field(..., ge=0, le=50, description="Number of web visits per month")
    Recency             :   int = Field(..., ge=0, le=365, description="Recency (days since last purchase)")


class BaseOutput(BaseModel):
    cluster_id      : int
    cluster_name    : str
    description     : str
    recommendation  : str


@app.get('/')
def Status():
    return {'message' : 'The api server is live and working'}


@app.post('/predict', response_model=BaseOutput)
def predict_segment(input_data: BaseInput):
    try:
        result = predict(
            age=input_data.Age,
            income=input_data.Income,
            total_spending=input_data.Total_Spendings,
            num_web_purchases=input_data.NumWebPurchases,
            num_store_purchases=input_data.NumStorePurchases,
            num_web_visits=input_data.NumWebVisitsMonth,
            recency=input_data.Recency
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error while predicting the output: {e}")