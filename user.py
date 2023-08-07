import numpy as np
import pickle
import streamlit as st
import pandas as pd


load_model=pickle.load(open("trained_model.pkl","rb"))
df_before_dummies= pd.read_csv("model_train.csv")


def full_input_data (data_before_dm,transmition="manual",input_data=[2007,0,214740.0]) :
  """predection for any data input to the model"""
  x=np.array(input_data)
  x=pd.DataFrame(x)
  x=x.transpose()
  x.columns=["Year","Fuel_type","Kms_Driven"]
  df1=pd.get_dummies(pd.DataFrame({'Transmission':[transmition]}))
  df1=df1.reindex(columns = pd.get_dummies(df_before_dummies["Transmission"],drop_first=True).columns, fill_value=0)
  new_test=pd.concat([x,df1],axis=1)
  prediction=load_model.predict(new_test)
  return prediction



def main () :
  #giving a title
  st.title('Car Pricing Predector')
  #getting the input data from the user

  Year = st.number_input('Year')
  Fuel_type = st.number_input('Fuel_type')
  Kms_Driven = st.number_input('Kms_Driven')

  Transmission =st.selectbox("Transmission",('manual', 'automatic', 'other'))
  #code for prediction
  price = ''
  #creating a button for prediction

  if st.button('Price of the Car:'):
    price = full_input_data(df_before_dummies,transmition= Transmission ,input_data=[Year,Fuel_type,Kms_Driven])
  st.success(price)



if __name__ == '__main__':
  main()