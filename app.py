import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from palani_svr import*


def predict_var(bend_angle, thickness):
   
    prediction=predict('Laser Forming.csv', bend_angle, thickness)
    print(prediction)
    return prediction



def main():
    st.title("Bendvision")
    html_temp = """
    <div style="background-color:#1c631f;padding:10px">
    <h2 style="color:white;text-align:center;">Prediction App </h2>
    <h6 style="color:white;text-align:center;"> Mechatronis and Instrumentation Lab IIT Indore </h6>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    bend_angle = st.text_input("Bend Angle")
    thickness = st.text_input("Thickness")

    if st.button("Predict"):
        result=predict_var(bend_angle, thickness)
        st.success(f"The output is Power : {result.iloc[0,0]}, Scan Speed : {result.iloc[0,1]}, SOD : {result.iloc[0,2]}")



if __name__=='__main__':
    main()
    
    
    