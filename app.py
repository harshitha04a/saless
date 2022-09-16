# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:11:05 2022

@author: harsh
"""


import pickle
import streamlit as st

  
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(year, km_driven, mileage, engine, max_power, age, Diesel, Electric, LPG, Petrol, Manual, seats5, more5seats):  
   
    prediction = classifier.predict(
        [[year, km_driven, mileage, engine, max_power, age, Diesel, Electric, LPG, Petrol, Manual, seats5, more5seats]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Car Price Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Classifier ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    year = st.text_input("year", "Type Here")
    km_driven = st.text_input("km_driven", "Type Here")
    mileage = st.text_input("mileage", "Type Here")
    engine = st.text_input("engine", "Type Here")
    max_power = st.text_input("max_power", "Type Here")
    age = st.text_input("age", "Type Here")
    Diesel = st.text_input("Diesel", "Type Here")
    Electric = st.text_input("Electric", "Type Here")
    LPG = st.text_input("LPG", "Type Here")
    Petrol = st.text_input("Petrol", "Type Here")
    Manual = st.text_input("Manual", "Type Here")
    seats5 = st.text_input("seats5", "Type Here")
    more5seats = st.text_input(">5seats", "Type Here")
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(float(year), float(km_driven), float(mileage), float(engine), float(max_power), float(age), float(Diesel), float(Electric), float(LPG), float(Petrol), float(Manual), float(seats5), float(more5seats))
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()
