import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_excel('file.xlsx')
st.write(df)

columns = ["Please inform us of how we could make the aforementioned topic more understandable and beneficial to all program participants? ",\
       "What is the reason for this rating?",\
       "What is the reason for this rating?.1", 
       "What is the reason for this rating?.2",
       "What is the reason for this rating?.3",
       "What is the reason for this rating?.4", 
        "Please elaborate on the aforementioned external factors affecting your performance, attendance, and/or overall progression in the program. Let us know how we can help. ",
        "Additional comments and/or notes:",
        "Is there a fellow or TKH staff member you would like to shine a light on this week? If so, who are they and why? (you can also choose yourself if applicable)"]

st.set_option('deprecation.showPyplotGlobalUse', False)
for col in columns:
  plt.subplot()
  df[f"response+{col}"].value_counts().plot.pie(figsize=(15,10))
  st.pyplot()