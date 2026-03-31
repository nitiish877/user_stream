%%writefile pallet.py
import streamlit as st
import seaborn as sea
import matplotlib.pyplot as plt
st.title("car crashes")
sea.get_dataset_names()
df=sea.load_dataset("car_crashes")
sea.scatterplot(data=df,x="alcohol",y="ins_losses")
st.write(df)
st.pyplot(plt)
