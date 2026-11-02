import streamlit as st


#setiing page
st.set_page_config(page_title="Cybersecurity E-Learning Portal")
#side bar
st.sidebar.title("Navigation")
menu=st.sidebar.radio("Go to:",["Home","Login/Sign in","Learning","Phishing Drill","Quiz"])

#choice if else
if menu == "Home":
  st.title("Welcome to the Cybersecurity Portal")
 # st.write(" Project.")
  st.info("Use the sidebar on the left to navigate the portal.")

elif menu == "Login/Sign in":
    st.title("Login/Sign in")
    st.write("hiba login and password strenght checker")
#ransomware
#torjan horse
#computer worm
#computer virus
elif menu == "Learning":
    st.title("Malware Learning Hub")
    st.write("To learn more click on any of the maliciuos program below...")
    # 1. Virus
    with st.expander("🦠 1. Computer Virus"):
      st.write("A malicious program that attaches itself to a clean file.")
     
      # This creates the tabs INSIDE the expander!
      tab1, tab2, tab3 = st.tabs(["How it spreads", "Real Example", "Prevention"])
    
      with tab1:
         st.write("Downloading infected files, sharing USB drives, and opening email attachments.")
      with tab2:
         st.write("The Melissa Virus (1999) spread through email and caused $80 million in damage.")
      with tab3:
        st.write("Don't download files from untrusted websites. Keep your antivirus updated.")

elif menu == "Phishing Drill":
    st.title("Live Phishing Drill")
    st.write("zia fake phishing emails+buttons")

elif menu == "Quiz":
    st.title("Cybersecurity Quiz")
    st.write("leena quiz+grading system")

