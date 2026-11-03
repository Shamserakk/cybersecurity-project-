import streamlit as st
import mysql.connector

def get_db_connection():
    try:
        # Securely grab the passwords from Streamlit's hidden vault
        conn = mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            port=st.secrets["mysql"]["port"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"],
            database=st.secrets["mysql"]["database"],
            ssl_ca="src/ca.pem" # (Assuming you uploaded the ca.pem file to the src folder)
        )
        return conn
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None
