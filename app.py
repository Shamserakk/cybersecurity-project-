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
    with st.expander("1.RANSOMWARE  "):
      st.write("A malicious program that attaches itself to a clean file.")  
     
      # This creates the tabs INSIDE the expander!
      tab1, tab2, tab3 = st.tabs(["What is ransomwares?", "How to protect yourself", "What if..."])
    
      with tab1:
         st.write("""Ransomware is a type of cyberattack that locks you out of your own computer files, devices, or networks. Attackers encrypt your data so you cannot use or access it, and then demand a payment—usually in cryptocurrency—to unlock it.
To make matters worse, modern hackers often use double extortion, meaning they also steal a copy of your private data and threaten to publish it online if you do not pay.""")
      with tab2:
         st.write("""• Regular Backups: Keeping isolated, offline backups.
• Consistent Updates: Patching systems immediately.
• Multi-Factor Authentication (MFA): Locking down accounts beyond just a password.""")
      with tab3:
        st.write("""• Isolate the Device: Immediately disconnect the infected computer from the Wi-Fi or local network to stop the virus from spreading.
• Do Not Pay the Ransom: Law enforcement (like the FBI or local cyber authorities) strongly advises against paying, as it funds criminal enterprises and marks you as an easy target.
• Report and Restore: Report the crime to authorities and attempt to wipe the system and restore data from a clean, pre-attack backup.")

elif menu == "Phishing Drill":
    st.title("Live Phishing Drill")
    st.write("zia fake phishing emails+buttons")

elif menu == "Quiz":
    st.title("Cybersecurity Quiz")
    st.write("leena quiz+grading system")

