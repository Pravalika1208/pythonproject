import streamlit as st

class Bank:
   def __init__(self):
       self.acbal = 10000

   def deposit(self):
       try:
           dep = st.number_input("Enter the deposit amount", min_value=100, step=100)

           if dep < 100:
               st.write("Minimum deposit amount should be 100")
           elif dep % 100 != 0:
               st.write("Deposit amount should be multiples of 100")
           elif dep > 50000:
               st.write("Maximum deposit amount should not exceed 50000")
           else:
               self.acbal += dep
               st.write(f"Successfully deposited {dep}. Current Balance: {self.acbal}")
       except ValueError:
           st.write("Invalid numeric input.")

   def withdraw(self):
       for attempt in range(3):
           try:
               wd = st.number_input("Enter the withdrawal amount", min_value=100, step=100)
               if wd < 100:
                   st.write("Minimum amount to withdraw is 100")
               elif wd % 100 != 0:
                   st.write("The withdrawal amount should be multiples of 100")
               elif wd > self.acbal - 500:
                   st.write("The withdrawal amount is exceeding the account balance")
               elif wd > 20000:
                   st.write("The maximum transaction limit is 20000")
               else:
                   self.acbal -= wd
                   st.write(f"Withdrawal successfully completed. Amount: {wd}. Current Balance: {self.acbal}")
                   break
           except ValueError:
               st.write("Invalid input. Enter a numeric value.")
       else:
           st.write("Maximum transaction attempts reached.")

   def balance_enquiry(self):
       st.write(f"Current Balance: {self.acbal}")

   def view_options(self):
       option = st.radio(
           "Choose an option:",
           ("Deposit", "Withdraw", "Balance Enquiry", "Exit")
       )

       if option == "Deposit":
           self.deposit()
       elif option == "Withdraw":
           self.withdraw()
       elif option == "Balance Enquiry":
           self.balance_enquiry()
       elif option == "Exit":
           st.write("Exiting the system")

   def validate(self):
       for attempt in range(3):
           try:
               pin = st.text_input("Enter the pin", type="password")
               if pin == "1234":
                   st.write("Successfully authenticated!")
                   self.view_options()
                   break
               else:
                   st.write("Invalid pin")
           except ValueError:
               st.write("Invalid input")
       else:
           st.write("Account blocked due to multiple failed attempts.")

# Create an instance of the bank and validate
obj = Bank()
obj.validate()