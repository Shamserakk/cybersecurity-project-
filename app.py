import streamlit as st
#sidebar menu
#st.sidebar.title("MENU")
#st.sidebar.write("Welcome To Our Portal")
#main title 
#st.title("Cybersecurity E-Learning Portal")
#st.write("Welcome!")
#
#st.success("system status:secure")
#st.warning("warning:phishing stimulator")
#section with button
#st.subheader('1.learning')
#st.write('virus,worms,torjan,ransomware')
#st.button("start") 
#st.subheader("2.phishing drill")
#st.write("test your skill")
#st.button("drill")"""

#setiing page
st.set_page_config(page_title="Cybersecurity E-Learning Portal")
#side bar
st.sidebar.title("Navigation")
menu=st.sidebar.radio("Go to:",["Home","Login/Sign in","Learning","Phishing Drill","Quiz"])

#choice if else
if menu == "Home":
  st.title("Welcome to the Cybersecurity Portal")
  st.write("This is the Class 12 Group Project.")
  st.info("Use the sidebar on the left to navigate the portal.")

elif menu == "Login/Sign in":
    st.title("Login/Sign in")
    st.write("Person 2 will write the Streamlit text boxes and password checker here.")

elif menu == "Learning":
    st.title("Malware Learning Hub")
    st.write("Learn about Viruses, Worms, Trojans, and Ransomware here.")

elif menu == "Phishing Drill":
    st.title("Live Phishing Drill")
    st.write("Person 3 will design the fake phishing emails and buttons here.")

elif menu == "Quiz":
    st.title("Cybersecurity Quiz")
    st.write("Person 4 will build the quiz questions and grading system here.")

