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

#computer worm
#computer virus
elif menu == "Learning":
  st.title("Malware Learning Hub")
  st.write("To learn more click on any of the maliciuos program below...")
    
  # 1. Virus
  with st.expander("1.RANSOMWARE  "):
      st.write("A malicious software that locks your computer files or devices and demands a payment to unlock them.")  
      # This creates the tabs INSIDE the expander!
      tab1, tab2, tab3 = st.tabs(["What is ransomwares?", "How to protect yourself", "What if..."])
      with tab1:
         st.write("""Ransomware is a type of cyberattack that locks you out of your own computer files, devices, or networks. Attackers encrypt your data so you cannot use or access it, and then demand a payment—usually in cryptocurrency—to unlock it. To make matters worse, modern hackers often use double extortion, meaning they also steal a copy of your private data and threaten to publish it online if you do not pay.""")
      with tab2:
         st.write("""• Regular Backups: Keeping isolated, offline backups.\n 
• Consistent Updates: Patching systems immediately.\n
• Multi-Factor Authentication (MFA): Locking down accounts beyond just a password.""")
      with tab3:
        st.write("""• Isolate the Device: Immediately disconnect the infected computer from the Wi-Fi or local network to stop the virus from spreading.\n
• Do Not Pay the Ransom: Law enforcement (like the FBI or local cyber authorities) strongly advises against paying, as it funds criminal enterprises and marks you as an easy target.\n
• Report and Restore: Report the crime to authorities and attempt to wipe the system and restore data from a clean, pre-attack backup.""")
 
  #torjan horse
  with st.expander("2.TORJAN HORSE "):
     st.write("one sentence")
     #tab inside expander
     tab1,tab2,tab3=st.tabs(["What is ransomwares?", "How to protect yourself", "What if..."])
     with tab1:
       st.write("""Trojan Horse (or Trojan) is a harmful computer program that tricks you by pretending to be something safe.\n 
       Just like the famous wooden horse from Greek history, it hides malicious software inside a disguised file—like a fake game, a helpful software update, or an email attachment. Once you open it, the virus sneaks into your system, allowing hackers to spy on you, steal your passwords, or damage your computer""")
     with tab2:
       st.write("""• Download Safely: Only get apps and files from official, trusted websites.\n
• Check Attachments: Never open unexpected files from unknown email senders.\n
• Use Antivirus: Keep a strong security program running to scan and block hidden threats.\n
• Update Regularly: Keep your operating system and apps updated to fix security flaws.""")
     with tab3:
       st.write("""• Disconnect from Internet: Turn off Wi-Fi immediately to stop hackers from stealing your data.\n
• Run a Security Scan: Use your antivirus software to find and delete the hidden threat.\n
• Change Your Passwords: Once the device is clean, update your logins from a different, safe device.""")
       
elif menu == "Phishing Drill":
    st.title("Live Phishing Drill")
    st.write("zia fake phishing emails+buttons")

elif menu == "Quiz":
    st.title("Cybersecurity Quiz")
    st.write("leena quiz+grading system")

