import streamlit as st
from src.database_helper import get_db_connection

def run_quiz(user_id=1):
    st.subheader("Cybersecurity Quiz")
    
    conn = get_db_connection()
    if not conn:
        return
        
    cursor = conn.cursor()
    cursor.execute("SELECT quiz_id, question, option_a, option_b, option_c, option_d, correct_answer FROM quizzes")
    questions = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not questions:
        st.warning("No questions found in the database.")
        return

    user_answers = {}
    st.write("Answer the questions below:")
    
    for q in questions:
        q_id, q_text, opt_a, opt_b, opt_c, opt_d, correct_opt = q
        options = [f"A) {opt_a}", f"B) {opt_b}", f"C) {opt_c}", f"D) {opt_d}"]
        
        choice = st.radio(
            label=f"**Question {q_id}:** {q_text}",
            options=options,
            index=None,
            key=f"q_{q_id}"
        )
        
        user_answers[q_id] = {
            'chosen_code': choice[0] if choice else None,
            'correct_code': correct_opt
        }
        st.write("---")
        
    if st.button("Submit Quiz", type="primary"):
        score = 0
        unanswered = False
        
        for q_id, ans_data in user_answers.items():
            if ans_data['chosen_code'] is None:
                unanswered = True
            elif ans_data['chosen_code'] == ans_data['correct_code']:
                score += 1
                
        if unanswered:
            st.warning("Please answer all questions before submitting.")
        else:
            percentage = (score / len(questions)) * 100
            st.success(f"🎉 Quiz Complete! Your Score: **{score} / {len(questions)}** ({percentage:.2f}%)")
            
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                try:
                    query = "INSERT INTO scores (user_id, score, total_questions, percentage) VALUES (%s, %s, %s, %s)"
                    values = (user_id, score, len(questions), percentage)
                    cursor.execute(query, values)
                    conn.commit()
                    st.info("Score successfully saved to the database leaderboard!")
                except Exception as e:
                    st.error(f"Failed to save score: {e}")
                finally:
                    cursor.close()
                    conn.close()
