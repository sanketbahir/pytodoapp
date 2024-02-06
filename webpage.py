import streamlit as st

st.title("Todo App")

col1, col2, col3 , col4, col5= st.columns([1, 2, 2, 1, 1])

with col1:
    if st.button("Add"):
        st.success("Add button clicked")

with col2:
    task_name = st.text_input("Add Task", "Enter task")

with col3:
    selected_date = st.date_input("Select Date")

with col4:
    if st.button("Update"):
        st.info("Update button clicked")

with col5:
    if st.button("Delete"):
        st.error("Delete button clicked")
