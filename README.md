# 🛒 Azure-based B2B Product Recommendation System

An end-to-end recommendation engine built on the Azure stack, simulating a B2B use case. It includes customer-specific and item-based recommendations, a Dash-powered internal dashboard.

I wish to demonstrate my skills on the Azure and Databricks platform through this project which I have tried to make as close to real production as possible without data from a real organization.

To make it as realistic as possible, I have asked ChatGPT 4o to act as my product owner and provide me with user stories. From these I have listed features I wish to include in a MVP.

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

## 📢 User stories

| **Role** | **User Story** | **Benefit** | 
| --- | --- | --- |
| **Sales Rep**         | As a sales rep, I want to see personalized product recommendations for each customer before a call, so I can pitch relevant products during my outreach. | Increases conversion by suggesting items customers are likely to buy. |
| **Sales Rep**         | As a sales rep, I want to be notified when a customer stops buying a recurring product, so I can suggest substitutes or follow up.                       | Prevents churn and maintains customer satisfaction.                   |
| **Sales Rep**         | As a sales rep, I want to see “similar customers also bought” items when placing orders, so I can upsell and cross-sell relevant products.               | Improves average order value (AOV).                                   |
| **Marketing Manager** | As a marketing manager, I want to identify product bundles frequently bought together by segment, so we can run targeted promotions.                     | Enables more effective and relevant campaigns.                        |
| **Marketing Manager** | As a marketing manager, I want to track engagement with recommended items in email campaigns, so I can fine-tune the recommendation logic.               | Helps optimize campaigns based on real behavior.                      |
| **E-commerce Lead**   | As an e-commerce manager, I want recommended items to appear in the B2B portal based on customer history, so buyers see what’s most relevant to them.    | Enhances digital customer experience and drives self-service sales.   |
| **Customer Support**  | As a support agent, I want to see suggested add-ons for a product when a customer calls in, so I can make helpful suggestions.                           | Boosts customer satisfaction and incidental sales.                    |
| **Procurement**       | As a procurement manager, I want to see forecasted demand for recommended items, so I can stock proactively.                                             | Reduces risk of stockouts on high-interest products.                  |
| **Sales Director**    | As a sales director, I want to see which reps are effectively using recommendations in their sales process, so I can identify best practices.            | Supports training and scaling of effective behaviors.                 |
| **IT / Data Team**    | As a data engineer, I want the recommendation engine to be retrained regularly with fresh data, so the suggestions stay accurate and up to date.         | Keeps the system effective and responsive to changes in demand.       |
| **B2B Buyer**         | As a B2B customer using the webshop, I want to see products relevant to my seasonal purchases, so I don't miss out on things I usually buy.              | Reduces friction and increases loyalty.                               |
| **B2B Buyer**         | As a B2B customer, I want to receive recommendations for new product lines that are relevant to my store profile, so I can stay competitive.             | Helps customers discover new and relevant products easily.            |

## 🤝 MVP Features

The stories are broken down into the following features that are being included in the MVP.

| **Feature** | **Description** | **Why MVP?** |
| --- | --- | --- |
| **1. Customer-specific Product Recommendations**     | Display top-N suggested products based on purchase history (costumer-based) | Core recommender engine to showcase personalization. |
| **2. "Others Also Bought" Suggestions**              | Recommend items that similar customers typically buy together (item-based) | Enables quick wins in upselling and cross-selling. |
| **3. Recommendation Dashboard** | Simple UI panel for sales reps to see recommendations per customer. | Easy to prototype; supports sales activities.         |
| **4. Static "Frequently Bought Together" Bundles**   | Show fixed sets of bundled items commonly bought together (based on historical data). | Quick to implement and very practical for campaigns |

## ⚙️ Tech stack and Architecture

For this MVP, I will use the tech stack as below.

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