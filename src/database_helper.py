
import streamlit as st
import mysql.connector
import tempfile

CA_CERT="""
-----BEGIN CERTIFICATE-----
MIIERDCCAqygAwIBAgIUeGBTkdwKm45lmjDHuGf6MTGITpowDQYJKoZIhvcNAQEM
BQAwOjE4MDYGA1UEAwwvMTc5YTdlZjAtN2JjYS00OTljLTk5MDktNDAxZDM0MTU3
M2YwIFByb2plY3QgQ0EwHhcNMjYxMTAyMTcyNzQzWhcNMzYxMDMwMTcyNzQzWjA6
MTgwNgYDVQQDDC8xNzlhN2VmMC03YmNhLTQ5OWMtOTkwOS00MDFkMzQxNTczZjAg
UHJvamVjdCBDQTCCAaIwDQYJKoZIhvcNAQEBBQADggGPADCCAYoCggGBAIhVx9Zf
Mug/r8ovfY7AXgyEPBkOyalV8A/adSqjCbCBYRSFBbmkoR3gY1BbzBw+oi3rXQDU
b3193B7aJ9yEC5n0eW4i9xwjZ6W8ro0Y+Ufgw941e3UIa9tYbSEMbCpQ0CE857qM
glE3/+WviblP3Y5hsS7J3N3BpgRLEaih8WRKnADxv7Z1LDKaBOspLW159qcuk17P
wHOZXfmh05mFz95MzknqkSExgrZ8n3CgZP12ACmQJ7p9hxZrPWW5S22TbzZftX3o
kTc/6CSOtXiGTDke8+moLWWsWQMdxxLvK9qLGZTJc6F7sZKCrBsMrbh3ai2c4Ri/
t4uI93GeYnVn0mWU+KqTLgCXpM3D7j6wNt71oXGgo2vwhfo0xgczEVQrqb56LU79
jjto4x4kV0NSfMJsQd0n4fkBj2Sy1S6n9bnsp94anQWM+fTw5W8VuCGXsh7ZpHlf
R5kyFqTD7F9/LFWw63f4L7tC2Eu2p2E6xPcAqQqOZN3uekX1XNyDTVxiewIDAQAB
o0IwQDAdBgNVHQ4EFgQUjjJl/CiqMoC01lCt/AHrzlEsjO8wEgYDVR0TAQH/BAgw
BgEB/wIBADALBgNVHQ8EBAMCAQYwDQYJKoZIhvcNAQEMBQADggGBAF/a4jA/QwYn
t5O7hvZ9oL7n7fO/XYNJmPjO4ZaTytYMb01aNQ8V0nSmnvK30ZCL+iTHUMVVqdGn
okTUU3Sz7ji7QjB3JDL42rsTVOdtIyq6diPs6oDJFE6hxogL2/tEiw35i1OVrBA0
O4UGAs/Me+OcDXP+kJdD9bLs9n8b3ThPyWPhF9t8wOtWqsq9CiAGKKqfqi4P65Lc
jGtOAxvPLpvlnVOZqDpSymFl+VWbBB+OuqFPLFbJmakPpSo/wU8u5UtElz5rsvPp
MVGxvvupsalbiKhhM1q65pr73C7tfEwelOdz1lOY8LO8pyOM27r+2t4//HyIhJUf
UDZB8LLH1wfO5eld8+HhcJQ8eQ/KWHpKswhOZySWGHjy8jkEaxsXPkCeFzthDgHk
xh36HtxHsZiU8QPryeo8fgbobLadgGZaXxd4dRpLyFoaasmCFcVoY/tygt9trKTh
UPxM7R/OZJAYCemt7rivsnO2e6LAexQhTDJ/mOKjAWWLAux98cmspw==
-----END CERTIFICATE-----
"""

def get_db_connection():
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pem") as temp_cert:
            temp_cert.write(CA_CERT.encode('utf-8'))
            temp_file_path = temp_cert.name

        conn = mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            port=st.secrets["mysql"]["port"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"],
            database=st.secrets["mysql"]["database"],
            ssl_ca=temp_file_path 
        )
        return conn
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None
