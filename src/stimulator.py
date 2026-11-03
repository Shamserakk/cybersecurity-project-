#zia codes here
import streamlit as st
import mysql.connector

def phishing_stimulator():
    st.subheader("Security Alert Simulation")
    
    # Fake email layout
    st.markdown("""
     **From:** security@g00gle.com  
     **Subject:** Urgent: Unusual sign-in attempt detected.  
     
     Dear User,  
     We noticed a login from an unrecognized device. Please verify your identity immediately to prevent account suspension.  
     [Verify Account Now](http://g00gle-security-check.com)
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        clicked = st.button("Click Link")
    with col2:
        reported = st.button("Report Phishing")
        
    if clicked:
        handle_failure()
    elif reported:
        st.success("Correct! You successfully identified the phishing attempt.")

def handle_failure():
    st.error("Oops! You fell for the phishing trap.")
    
    st.markdown("### Red Flags You Missed:")
    st.markdown("* **Spoofed Domain:** Look closely at the sender address—it uses zeros (`g00gle.com`) instead of 'oo'.")
    st.markdown("* **Urgency & Fear:** Legitimate services rarely threaten immediate account suspension via email links.")
    
    # Call database function
    save_failure_to_db()

def save_failure_to_db():
    try:
        # Connect to your MySQL database
        # Streamlit will look for these values inside the hidden secrets.toml file
        db = mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
        )
        cursor = db.cursor()

        # SQL Insert Command
        query = "INSERT INTO drill_logs (action_type, status) VALUES (%s, %s)"
        values = ("Clicked Phishing Link", "Failed")
        
        cursor.execute(query, values)
        db.commit()
        
        cursor.close()
        db.close()
        st.info("Failure record logged to the database.")
        
    except Exception as e:
        st.error(f"Database connection failed: {e}")
