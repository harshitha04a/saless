# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:59:03 2022

@author: harsh
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open("C:/Users/harsh/myfile.sav","rb"))
def first(input_data):
    input_array=np.asarray(input_data)
    y=loaded_model.predict(input_array.reshape(1,-1))
    return y
def main():
    st.title("selling price prediction")
    year=st.text_input("enter year")
    kn_driven=st.text_input("driven_km")
    mileage=st.text_input("mileage")
    engine=st.text_input("engine")
    max_power=st.text_input("max_power")
    age=st.text_input("entr age")
    diesel=st.radio("enter diesel or not","01")
    if diesel==0:
        st.write(0)
    elif diesel==1:
        st.write(1)
    electric=st.radio("enter electric","01")
    if electric==0:
        st.write(0)
    elif electric==1:
        st.write(1)
    lpg=st.radio("enter lpg","01")
    if lpg==0:
        st.write(0)
    elif lpg==1:
        st.write(1)
    petrol=st.radio("enter petrol","01")
    if petrol==0:
        st.write(0)
    elif petrol==1:
        st.write(1)
    manual=st.radio("enter manual","01")
    if manual==0:
        st.write(0)
    elif manual==1:
        st.write(1)
    fiveseats=st.radio("enter 5 seats or not","01")
    if fiveseats==0:
        st.write(0)
    elif fiveseats==1:
        st.write(1)
    gt5seats=st.radio("greater than 5 seats or not","01")
    if gt5seats==0:
        st.write(0)
    elif gt5seats==1:
        st.write(1)
    diagnosis=''
    if st.button("price prediction"):
        diagnosis=first([float(year),float(kn_driven),float(mileage),float(engine),float(max_power),float(age),float(diesel),float(electric),float(lpg),float(petrol),float(manual),float(fiveseats),float(gt5seats)])
    st.success(diagnosis)
if __name__=='__main__':
    main()