### Date created
28th Oct 2022

### Project Title
**Used Car Price Prediction using Linear & Lasso Regression**

### Description
Linear Regression performs the task to predict a dependent variable value (y) based on a given independent variable (x).
Lasso Regression is a regression analysis method that performs both variable selection and regularization in order to enhance the prediction accuracy and interpretability of the resulting statistical model.

For this project, we will be building a machine learning model to prefict the price of a used car based on certain data included in the dataset. Our goal is to work through this notebook by collecting data, preprocessing it, splitting it into testing and training datasets, train the model and evaluate the accuracy of our model.

**API**

We have created an API using FastAPI for users to interact with.
You can run the model using uvicorn on your local machine and test the API, refer to car_price_api.py.

```
uvicorn car_price_api:app --reload
```

**StreamLit Web App**

We also created a simple web app using Streamlit.
You can run the app on your local machine using StreamLit and test the web app, refer to car_price_streamlit.py.

```
streamlit run car_price_streamlit.py
```

### Files used
We used the following dataset available on Kaggle to work on this project:

* [Vehicle dataset](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)

The datasets consists of several predictor variables and one target variable, selling price. Predictor variables includes the manufacturing year, distance driven, fuel type, seller type, transmission type and so on.

### Credits
Thanks to Kaggle for teaching me ML :sparkles: :heart: :sparkles:
