import streamlit as st

price = st.number_input("Enter Product Price: ")
discount_percentage = st.slider("Select Percentage Discount",0,50,0)
calc_disc = st.button("Calculate")
result = 0
table = list()
if calc_disc:
    result = price*(1-discount_percentage/100)
    st.write(f"Final Price: {result}")
table.append([f"Before = {price}",f"After = {result}"])
st.table(table)


