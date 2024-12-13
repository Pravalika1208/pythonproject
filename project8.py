import streamlit as st
st.title("Employee shopping bill")
sal=st.number_input("enter employee salary:")
sp1=st.number_input("enter shopping bill1:")
sp2=st.number_input("enter shopping bill2:")
sp3=st.number_input("enter shopping bill3:")
if st.button("Total_bill"):
   total=sp1+sp2+sp3
   per=(total/sal)*100
   st.write(total)
   st.write("amount spent on shopping in percentage: ",per,"%")project8.py