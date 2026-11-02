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

elif menu == "Learning":
  st.title("Malware Learning Hub")
  st.write("To learn more click on any of the maliciuos program below...")
    
  # 1. Virus
  with st.expander("RANSOMWARE  "):
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
  with st.expander("TORJAN HORSE "):
     st.write("A Trojan Horse is a fake computer program that tricks you into opening it so hackers can sneak in and steal your data.")
     #tab inside expander
     tab1,tab2,tab3=st.tabs(["What is ransomwares?", "How to protect yourself", "What if..."])
     with tab1:
       st.write("""Trojan Horse (or Trojan) is a harmful computer program that tricks you by pretending to be something safe.Just like the famous wooden horse from Greek history, it hides malicious software inside a disguised file—like a fake game, a helpful software update, or an email attachment. Once you open it, the virus sneaks into your system, allowing hackers to spy on you, steal your passwords, or damage your computer""")
     with tab2:
       st.write("""• Download Safely: Only get apps and files from official, trusted websites.\n
• Check Attachments: Never open unexpected files from unknown email senders.\n
• Use Antivirus: Keep a strong security program running to scan and block hidden threats.\n
• Update Regularly: Keep your operating system and apps updated to fix security flaws.""")
     with tab3:
       st.write("""• Disconnect from Internet: Turn off Wi-Fi immediately to stop hackers from stealing your data.\n
• Run a Security Scan: Use your antivirus software to find and delete the hidden threat.\n
• Change Your Passwords: Once the device is clean, update your logins from a different, safe device.""")

  #computer worm
  with st.expander("COMPUTER WORM "):
    st.write("A computer worm is a self-copying virus that automatically crawls from one device to another to slow down networks and damage files.")
    tab1,tab2,tab3=st.tabs(["What is ransomwares?", "How to protect yourself", "What if..."])
    with tab1:
      st.write("""• Install Updates Immediately: Keep your operating system and apps updated to patch the network flaws worms use to travel.\n
• Enable Your Firewall: A strong firewall acts as a digital shield, blocking unauthorized traffic and stopping worms from sneaking in.\n
• Use Modern Antivirus: Ensure your security software is active and capable of scanning network traffic.is a harmful virus that copies itself and spreads automatically from device to device without you doing anything. Unlike a Trojan, which requires you to open it, a worm sneaks in through security loopholes in a network. Once inside, it travels quietly to other connected computers, slowing down networks and damaging files as it goes.""")
    with tab2:
      st.write("""• Install Updates Immediately: Keep your operating system and apps updated to patch the network flaws worms use to travel.\n
• Enable Your Firewall: A strong firewall acts as a digital shield, blocking unauthorized traffic and stopping worms from sneaking in.\n
• Use Modern Antivirus: Ensure your security software is active and capable of scanning network traffic.""")
    with tab3:
      st.write("""• Isolate the Device: Unplug your internet cable or turn off Wi-Fi instantly so the worm cannot spread to your router or other devices in the house.\n
• Run a Full Scan: Use your antivirus tool to locate and permanently delete the worm.\n
• Patch the System: Figure out how the worm got in and update that specific software right away.""")

  #computer virus
  with st.expander("COMPUTER VIRUS"):
    st.write("A computer virus is a harmful program that hides inside normal files and spreads to other devices only when a user opens or shares the infected file.")
    tab1,tab2,tab3=st.tabs(["What is ransomwares?", "How to protect yourself", "What if..."])
    with tab1:
      st.write("""A computer virus is a harmful program that hitches a ride on safe files and needs you to open it to spread. Unlike a worm (which travels by itself), a virus is lazy—it hides inside an everyday file, like a document or a USB drive. It stays asleep until you click it open. Once activated, it copies itself into your other files, corrupts your data, and hitches a ride to other computers when you share files.""")
    with tab2:
      st.write("""• Scan USBs First: Always scan external drives with antivirus software before opening them.\n
• Avoid Shady Files: Never download attachments or software from unverified websites.\n
• Run Antivirus: Keep reliable security software running to catch threats before they open.""")
    with tab3:
      st.write("""• Stop Sharing Files: Do not email files or use USBs, or you will pass the virus to others.\n
• Run a System Scan: Use your antivirus software to find, trap, and delete the virus.""")

  #phishing
  with st.expander("PHISHING"):
    st.write("Phishing is when hackers send fake emails or texts to trick you into stealing your passwords or money.")
    tab1,tab2,tab3=st.tabs(["What is ransomwares?", "How to protect yourself", "What if..."])
    with tab1:
      st.write("""Phishing is a scam where hackers trick you into giving up private information by pretending to be a company or person you trust. Instead of using sneaky code, it tricks human nature. Attackers send fake emails or texts that look exactly like your bank, a streaming service, or a delivery company. They create a false sense of urgency—claiming your account is locked or a package is missing—to scare you into clicking a link and typing your passwords or credit card details into a fake website.""")
    with tab2:
      st.write("""• Check the Sender: Look closely at the email address. Scammers use slight typos (like support@paypa1.com instead of paypal.com).\n
• Ignore the Panic: Be skeptical of messages demanding immediate action or threatening account suspension.\n
• Type the URL: Never click links inside suspicious emails. Type the official website address directly into your browser.""")
    with tab3:
      st.write("""• Change Passwords Fast: If you typed your password into a sketchy page, change it immediately across all accounts.\n
• Alert Your Bank: If you shared banking details, call your bank right away to freeze your cards.""")

elif menu == "Phishing Drill":
    st.title("Live Phishing Drill")
    st.write("zia fake phishing emails+buttons")

elif menu == "Quiz":
    st.title("Cybersecurity Quiz")
    st.write("leena quiz+grading system")

