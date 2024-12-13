import streamlit as st
st.title("Gross salary calculator")
basic_salary=st.number_input("enter your basic salary:",min_value=0,step=1)
if st.button("Calculate Gross Salary"):
   hra=0
   da=0
   if basic_salary<10000:
       hra = (67 / 100) * basic_salary
       da = (73 / 100) * basic_salary
   elif basic_salary<20000:
       hra = (69 / 100) * basic_salary
       da = (76 / 100) * basic_salary
   else:
       hra = (73 / 100) * basic_salary
       da = (89 / 100) * basic_salary
   gross=hra+da+basic_salary
   st.write(gross)
