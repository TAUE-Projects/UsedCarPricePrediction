import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("model_train.csv")
    return data

data = load_data()

# Preprocess data
X = data.drop("price", axis=1)
y = data["price"]

# Convert categorical variables into dummy/indicator variables
X = pd.get_dummies(X, columns=["Car_Name", "Fuel_type", "Transmission"], drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)


import streamlit as st
import pandas as pd

# Custom HTML and CSS for styling
html_template = """
<style>
/* Styling for the application title */
.stAppTitle {
    text-align: center;
    font-size: 2.5rem;
    color: #007bff;
    margin-bottom: 2rem;
}

/* Styling for the predicted price text */
.stPredictedPrice {
    text-align: center;
    font-size: 1.5rem;
    color: #00c853;
    margin-top: 2rem;
}
</style>
"""
st.markdown(html_template, unsafe_allow_html=True)


page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://images.pexels.com/photos/1534604/pexels-photo-1534604.jpeg?auto=compress&cs=tinysrgb&w=1600");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit web app
st.title("Car Price Prediction")

# Sidebar for user input
st.sidebar.header("Enter Car Details")

car_names = X_train.filter(like='Car_Name').columns
car_name = st.sidebar.selectbox("Car Name", car_names, key="car_name")

year = st.sidebar.number_input("Year", min_value=1990, max_value=2023, value=2020)
kms_driven = st.sidebar.number_input("Kms Driven", min_value=0, value=50000)

fuel_types = X_train.filter(like='Fuel_type').columns
fuel_type = st.sidebar.selectbox("Fuel Type", fuel_types)

transmissions = X_train.filter(like='Transmission').columns
transmission = st.sidebar.selectbox("Transmission", transmissions)

# "Predict" button
predict_button = st.sidebar.button("Predict", key="predict_button")

if predict_button:
    # Preprocess user input
    input_data = {
        "Year": [year],
        "Kms_Driven": [kms_driven],
    }
    for col in car_names:
        input_data[col] = [1 if col == car_name else 0]
    for col in fuel_types:
        input_data[col] = [1 if col == fuel_type else 0]
    for col in transmissions:
        input_data[col] = [1 if col == transmission else 0]

    input_df = pd.DataFrame(input_data)

    # Make prediction
    prediction = abs(model.predict(input_df))

    # Display prediction with styling
    st.markdown(
        f"The predicted price for the selected car is: **${prediction[0]:,.2f}**",
        unsafe_allow_html=True,
    )


