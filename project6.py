import streamlit as st
st.title("Student Grade")
proj=st.number_input("enter project score:")
intern=st.number_input("enter internal score:")
ext=st.number_input("enter external score:")
if st.button("Calculate grade"):
   if proj>=50 and intern>=50 and ext>=50:
       total=(70/100)*proj+(10/100)*intern+(20/100)*ext
       if total>=90:
           st.write("A grade")
       elif total>80:
           st.write("B grade")
       elif total>70:
           st.write("C grade")
       else:
           st.write("D grade")
   else:
       if proj<50:
           st.write("failed in project and score is:",proj)
       if ext<50:
           st.write("failed in external and score is:",ext)
       if intern<50:
           st.write("failed in internal and score is:",intern)