import streamlit as st
# Password Checker
def check_password(password):
    if len(password) < 8:
        return "Weak: Minimum 8 characters required"
    if not any(ch.isupper() for ch in password):
        return "Weak: Add an uppercase letter"
    if not any(ch.isdigit() for ch in password):
        return "Weak: Add a number"
    if not any(not ch.isalnum() for ch in password):
        return "Weak: Add a special symbol"
    return "Strong Password!"
    
# Main
def auth_page():
    st.header("Account Access")
    tab_signup, tab_login = st.tabs(["Signup", "Login"])

    # SIGNUP TAB 
    with tab_signup:
        st.subheader("Create an Account")
        new_user = st.text_input("Username", key="signup_user")
        new_pass = st.text_input("Create Password", type="password", key="signup_pass")

        if st.button("Signup"):
            if new_user.strip() == "" or new_pass == "":
                st.error("Please fill all fields.")
            else:
                # Check the password
                result = check_password(new_pass)
                
                if result == "Strong Password!":
                    #connect to database
                    db=get_db_connection()
                    if conn:
                        cursor=db.cursor()
                        try:
                            query="insert into user(username,password) values (%s,%s)"
                            values=(new_user,new_pass)
                            cursor.execute(query,values)
                            db.commit()
                            st.success(f"Account created for {new_user}!")
                        except Exception as e:
                            st.error(f"ERROR:Username might already exist.")
                        finally:
                            cursor.close()
                            db.close()
                else:
                    st.warning(result)

    #LOGIN TAB
    with tab_login:
        st.subheader("Login to Your Account")
        login_user = st.text_input("Username", key="login_user")
        login_pass = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            if login_user.strip() == "" or login_pass == "":
                st.error("Please fill all fields.")
            else:
                # PLACEHOLDER: We will add MySQL SELECT here later comparing username and password in the table with the given
                db=get_db_connection()
                if db:
                    cursor=db.cursor()
                    query="select * from users where username=%s and password=%s"
                    values=(login_user,login_pass)
                    cursor.execute(query,values)
                    user=cursor.fetchone()
                    cursor.close()
                    db.close()
                    if user:
                        st.success(f"Welcome back,{login_user}!")
                    else:
                        st.error("Invalid Username or Password.")
