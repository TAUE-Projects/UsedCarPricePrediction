# UsedCarPricePrediction

Data Overview and Preprocessing
In this section, we present an overview of the dataset used for our analysis and the preprocessing steps undertaken to ensure data quality and accuracy. The dataset consists of two main components: the original data and the processed data after performing data preparation techniques, including handling missing values.

1. Dataset Description
The original dataset comprises a total of 290,129 entries for the training set and 124,341 entries for the test set. Each entry represents a distinct observation, and there are 20 features (columns) in the training set and 19 features in the test set, including information related to the vehicles such as year, manufacturer, model, condition, cylinders, fuel type, odometer reading, title status, transmission, drive type, size, type, paint color, state, latitude, longitude, and posting date.

2. Missing Value Analysis
During the initial inspection of the data, we identified missing values across multiple features in both the training and test datasets. Missing values can introduce biases and inaccuracies in our analysis and predictive modeling. The number of missing values for each feature in the original training dataset is as follows:

"Unnamed: 0": 0 missing values.
"id": 0 missing values.
"year": 0 missing values.
"manufacturer": 11,342 missing values.
"model": 0 missing values.
"condition": 116,104 missing values.
"cylinders": 119,300 missing values.
"fuel": 1,453 missing values.
"odometer": 0 missing values.
"title_status": 5,066 missing values.
"transmission": 0 missing values.
"drive": 88,087 missing values.
"size": 207,684 missing values.
"type": 62,596 missing values.
"paint_color": 87,113 missing values.
"state": 0 missing values.
"lat": 4,403 missing values.
"long": 4,403 missing values.
"posting_date": 0 missing values.
3. Data Preparation and Handling Missing Values
To address the issue of missing values, we employed data preparation techniques to clean and preprocess the dataset. The steps involved identifying the nature of missingness for each feature and determining the most appropriate method to handle them.

We opted for a method known as data imputation to fill in the missing values. For numeric features such as "cylinders," "size," and "lat," we utilized the mean of the available values to impute the missing ones. This approach ensures that the imputed values are close to the existing distribution, minimizing distortion in the data.

For categorical features such as "manufacturer," "condition," "fuel," "title_status," "drive," "type," "paint_color," and "posting_date," we adopted the mode imputation method. By using the mode (most frequently occurring value) of each categorical feature, we preserved the dominant category, enhancing the representativeness of the imputed data.

4. Final Processed Dataset
After completing the data preprocessing steps, we derived a final processed dataset that contains 290,129 entries for the training set and 124,341 entries for the test set. The processed training dataset comprises 15 columns, while the processed test dataset consists of 14 columns. All missing values have been appropriately imputed, resulting in a clean and ready-to-use dataset for our analysis and modeling tasks.

