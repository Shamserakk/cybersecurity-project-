import streamlit as st
from src.database_helper import get_db_connection

def phishing_simulator(user_id=1):
    st.subheader("🎣 Live Phishing Drill")
    st.write("Select a simulation below and test your ability to spot a scam.")
    
    scenario = st.selectbox(
        "Choose an Email to Analyze:",
        ["Scenario 1: The Fake Google Alert", 
         "Scenario 2: The Fake Password Reset", 
         "Scenario 3: The Legitimate Notification"]
    )
    
    st.divider()

    if scenario == "Scenario 1: The Fake Google Alert":
        st.markdown("""
        > **From:** security@g00gle.com  
        > **Subject:** Urgent: Unusual sign-in attempt detected.
        > 
        > Dear User,
        > We noticed a login from an unrecognized device. Please verify your identity immediately to prevent account suspension.
        > 
        > **[Verify Account Now](http://g00gle-security-check.com)**
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Click Link", key="s1_click"):
                handle_failure(user_id, "Clicked g00gle link", [
                    "**Spoofed Domain:** Look closely at the sender address—it uses zeros (`g00gle.com`) instead of 'oo'.",
                    "**Urgency & Fear:** Legitimate services rarely threaten immediate account suspension.",
                    "**Unencrypted Link:** The link starts with 'http://' instead of the secure 'https://'."
                ])
        with col2:
            if st.button("Report Phishing", key="s1_report"):
                st.success("Correct! You successfully identified the phishing attempt.")

    elif scenario == "Scenario 2: The Fake Password Reset":
        st.markdown("""
        > **From:** support@paypaI-alerts.com  
        > **Subject:** ACTION REQUIRED: Your account has been locked!  
        > 
        > Dear Customer,  
        > We detected multiple failed login attempts on your account. For your safety, your account access has been restricted.  
        > Click the link below to verify your identity and restore access immediately:  
        > **[Restore My Account Now](http://paypai-security-verify.com/login)**
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Click Link", key="s2_click"):
                handle_failure(user_id, "Clicked paypaI link", [
                    "**Lookalike Letters:** `paypaI` uses a capital **i** instead of a lowercase **L**.",
                    "**Fake Link Domain:** The link points to `paypai-security-verify.com`, not `paypal.com`."
                ])
        with col2:
            if st.button("Report Phishing", key="s2_report"):
                st.success("Spot on! This was a fake password reset request.")

    elif scenario == "Scenario 3: The Legitimate Notification":
        st.markdown("""
        > **From:** no-reply@accounts.google.com  
        > **Subject:** Security alert for your linked Google Account  
        > 
        > Your Google Account was just signed in to from a new Windows device.  
        > You can check activity by going directly to your account settings at **myaccount.google.com**.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Mark as Safe", key="s3_safe"):
                st.success("Correct! This is a legitimate notification from Google's real domain.")
        with col2:
            if st.button("Report Phishing", key="s3_report"):
                st.warning("False Alarm! This email came from the official `@accounts.google.com` domain and doesn't ask you to click suspicious links.")

def handle_failure(user_id, activity_name, red_flags):
    st.error("Oops! You fell for the trap.")
    st.markdown("### Red Flags You Missed:")
    for flag in red_flags:
        st.markdown(f"* {flag}")
    save_failure_to_db(user_id, activity_name)

def save_failure_to_db(user_id, activity_name):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO simulation_logs (user_id, activity) VALUES (%s, %s)"
            values = (user_id, activity_name)
            cursor.execute(query, values)
            conn.commit()
            st.info("Failure record logged to the database.")
        except Exception as e:
            st.error(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()
