import streamlit as st
"""sidebar menu
st.sidebar.title("MENU")
st.sidebar.write("Welcome To Our Portal")
#main title 
st.title("Cybersecurity E-Learning Portal")
st.write("Welcome!")
#
st.success("system status:secure")
st.warning("warning:phishing stimulator")
#section with button
st.subheader('1.learning')
st.write('virus,worms,torjan,ransomware')
st.button("start") 
st.subheader("2.phishing drill")
st.write("test your skill")
st.button("drill")"""

#setiing page
st.set_page_config(page_title="Cybersecurity E-Learning Portal")
#side bar
st.sidebar.title("Navigation")
menu=st.sidebar.radio("Go to:",["Home","Login/Sign in","Learning","Phishing Drill","Quiz"])
