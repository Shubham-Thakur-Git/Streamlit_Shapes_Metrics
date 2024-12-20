import pandas as pd
import numpy as np
import streamlit as st
import math

from PIL import Image

st.title("Calculate Metrics of given shapes")

# Create a dropdown (select box)
options = ["Select an option","Circle", "Triangle", "Cylinder", "Rectangle"]
selected_option = st.selectbox("Choose a shape:", options)

def show_shape(shape):
    img = Image.open(fr"C:\Users\thaku\Documents\MacBook\Shubham's Stuff\Naresh IT\Data_Science_AI_Omkar Sir\VSCode\{shape}.png")
    st.image(img, caption=f'{shape}', use_column_width=True)

# Display the selected option
if selected_option != "Select an option":
    st.write(f"You selected: {selected_option}")

    if selected_option == 'Circle':
        options1 = ["Select an option","Area","Circumference"]
        selected_option1 = st.selectbox("What do you want to calculate:", options1)
        if selected_option1 == 'Area':
            radius = st.text_input("Enter Radius:", placeholder="cms")
            if st.button("Submit"):
                area = math.pi*eval(radius)*eval(radius)
                st.success(area)
                show_shape(selected_option)
        elif selected_option1 == 'Circumference':
            radius = st.text_input("Enter Radius:", placeholder="cms")
            if st.button("Submit"):
                circumference = 2*math.pi*eval(radius)
                st.success(circumference)
                show_shape(selected_option)
        else:
            st.write("Please select an option.")

    
    if selected_option == 'Triangle':
        options1 = ["Select an option","Area"]
        selected_option1 = st.selectbox("What do you want to calculate:", options1)
        if selected_option1 == 'Area':
            height = st.text_input("Enter height:", placeholder="cms")
            base = st.text_input("Enter base:", placeholder="cms")
            if st.button("Submit"):
                area = 0.5*eval(height)*eval(base)
                st.success(area)
                show_shape(selected_option)
        else:
            st.write("Please select an option.")


    if selected_option == 'Cylinder':
        options1 = ["Select an option","Surface Area","Volume"]
        selected_option1 = st.selectbox("What do you want to calculate:", options1)
        if selected_option1 == 'Surface Area':
            radius = st.text_input("Enter Radius:", placeholder="cms")
            height = st.text_input("Enter Height:", placeholder="cms")
            if st.button("Submit"):
                surface_area = 2*(math.pi)*eval(radius)*eval(height) + 2*(math.pi)*eval(radius)*eval(radius)
                st.success(surface_area)
                show_shape(selected_option)
        elif selected_option1 == 'Volume':
            radius = st.text_input("Enter Radius:", placeholder="cms")
            height = st.text_input("Enter Height:", placeholder="cms")
            if st.button("Submit"):
                volume = math.pi*eval(radius)*eval(radius)*eval(height)
                st.success(volume)
                show_shape(selected_option)
        else:
            st.write("Please select an option.")


    if selected_option == 'Rectangle':
        options1 = ["Select an option","Area","Circumference"]
        selected_option1 = st.selectbox("What do you want to calculate:", options1)
        if selected_option1 == 'Area':
            length = st.text_input("Enter length:", placeholder="cms")
            width = st.text_input("Enter width:", placeholder="cms")
            if st.button("Submit"):
                area = eval(length)*eval(width)
                st.success(area)
                show_shape(selected_option)
        elif selected_option1 == 'Circumference':
            length = st.text_input("Enter length:", placeholder="cms")
            width = st.text_input("Enter width:", placeholder="cms")
            if st.button("Submit"):
                circumference = 2*(eval(length)+eval(width))
                st.success(circumference)
                show_shape(selected_option)
        else:
            st.write("Please select an option.")
  

else:
    st.write("Please select an option.")