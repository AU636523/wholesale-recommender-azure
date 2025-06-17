# 🛒 Azure-based B2B Product Recommendation System

An end-to-end recommendation engine built on the Azure stack, simulating a B2B use case. It includes customer-specific and item-based recommendations, a Dash-powered internal dashboard.

<<<<<<< HEAD
## Tech Stack
Implemented with Azure Databricks native tools, such as PySpark
=======
To make it as realistic as possible, I have asked ChatGPT 4o to act as my product owner and provide me with user stories. From these I have listed features I wish to include in a MVP.
>>>>>>> 57fc06cb21112f6624777dc874ebd711ea11832f

## 📁 Project Structure

```bash
📦 wholesale-recommender-azure
├── data/              # Input data
├── notebooks/         # Azure Databricks notebooks for data prep, modeling, scoring
├── models/            # Exported models
├── dashboards/        # Dash app
├── pipeline/          # Code for automated batch pipelines
├── docs/              # Diagrams and visuals
├── requirements.txt   # Python packages
└── README.md
```

## ⚙️ Considerations for putting into production

The recommended tech stack below supports weekly data ingestion and retraining of models

| **Requirement** | **Azure Technology / Service** |
| --- | --- |
| Store raw data (transactions, products, costumers) | Azure Data Lake Storage Gen2 |
| Preprocessing and Feature Generation | Azure Databricks + PySpark |
| Train recommender model (customer-based) | Azure Databricks |
| Train recommender model (item-based) | Azure Databricks | 
| Generate static product bundles | Azure Databricks |
| Handle requests, routing etc. (batch processed results) | Azure Functions |
| Serve model | Azure Machine Learning Endpoints (API) |
| Display internal dashboard with customer recommendations | Plotly Dash ( Azure App Service) |
| Visualize product recommendation usage and trends | PowerBI |
| Automate model retraining and batch scoring | Azure ML Pipelines |
| Version control and deployment automation | GitHub + Azure DevOps |

## Data

Data obtained from the open source data set: https://www.kaggle.com/datasets/gabrielsantello/wholesale-and-retail-orders-dataset/
