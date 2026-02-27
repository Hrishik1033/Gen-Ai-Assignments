import streamlit as st

name = st.sidebar.text_input("Enter Product Name: ",placeholder='Product Name....')
category = st.sidebar.selectbox("Category",('Soft Drinks','Food','Toys','Decorative Items'))
price = st.sidebar.number_input("Enter Price: ",placeholder='Price...')
button = st.sidebar.button("Add Product")
details = list()
if button:
    st.write("Success... Product Added")
    details.append([f"Priduct Name: {name}",f"Product Category: {category}",f"Product Price: {price}"])
    st.table(details)