import streamlit as st
from src.database_helper import get_db_connection

def create_tables():
    conn = get_db_connection()
    if not conn:
        return
        
    cursor = conn.cursor()
    
    # The SQL code (Note: No semicolons inside, we split by semicolon below)
    sql_script = """
    CREATE TABLE IF NOT EXISTS users (user_id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(255) NOT NULL);
    CREATE TABLE IF NOT EXISTS quizzes (quiz_id INT AUTO_INCREMENT PRIMARY KEY, question TEXT NOT NULL, option_a VARCHAR(255) NOT NULL, option_b VARCHAR(255) NOT NULL, option_c VARCHAR(255) NOT NULL, option_d VARCHAR(255) NOT NULL, correct_answer CHAR(1) NOT NULL, topic VARCHAR(100));
    CREATE TABLE IF NOT EXISTS scores (score_id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL, score INT NOT NULL, total_questions INT NOT NULL, percentage DECIMAL(5,2), quiz_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE);
    CREATE TABLE IF NOT EXISTS simulation_logs (log_id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL, activity VARCHAR(255) NOT NULL, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE);
    drop table quizzes;
    
    """

    # Split the script by semicolons and run each command
    statements = sql_script.split(';')
    try:
        for statement in statements:
            if statement.strip():
                cursor.execute(statement)
        conn.commit()
        st.success("Database tables and questions created successfully!")
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
