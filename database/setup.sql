#1. USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

#2. QUIZZES TABLE (From Naja)
CREATE TABLE IF NOT EXISTS quizzes (
    quiz_id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_answer CHAR(1) NOT NULL,
    topic VARCHAR(100)
);

#3. SCORES TABLE (From Naja)
CREATE TABLE IF NOT EXISTS scores (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    score INT NOT NULL,
    total_questions INT NOT NULL,
    percentage DECIMAL(5,2),
    quiz_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

#4. SIMULATION LOGS TABLE (For the Phishing Drill)
CREATE TABLE IF NOT EXISTS simulation_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    activity VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

#5. INSERT THE QUIZ QUESTIONS (From Naja)
INSERT INTO quizzes (question, option_a, option_b, option_c, option_d, correct_answer, topic)
VALUES
('What is phishing?', 'A computer game', 'A trick to steal sensitive information', 'A programming language', 'A search engine', 'B', 'Phishing'),
('What is malware?', 'A malicious software', 'A computer accessory', 'A browser', 'A website', 'A', 'Malware'),
('What should you do with a suspicious email link?', 'Click it', 'Share it', 'Verify the sender before clicking', 'Enter your password', 'C', 'Phishing'),
('Which is a strong password practice?', 'Using 123456', 'Using your name', 'Using the same password everywhere', 'Using long and unique passwords', 'D', 'Password Security'),
('What does HTTPS indicate?', 'The website is guaranteed safe', 'The connection is encrypted', 'The website is virus-free', 'The website is government-owned', 'B', 'Web Security'),
('What is two-factor authentication?', 'Using two usernames', 'Having two email accounts', 'An additional identity verification step', 'Changing passwords twice', 'C', 'Authentication'),
('What should you do if you receive an unexpected OTP?', 'Share it', 'Post it online', 'Send it to a friend', 'Never share it and verify the request', 'D', 'OTP Security'),
('What is a computer virus?', 'A type of malware that can infect files or programs', 'A keyboard', 'A browser', 'A monitor', 'A', 'Malware'),
('Why are software updates important?', 'They change wallpapers', 'They fix security vulnerabilities', 'They remove passwords', 'They stop internet access', 'B', 'Cybersecurity'),
('What should you check before entering information on a website?', 'Its background colour', 'Its font style', 'Its address and legitimacy', 'Its number of images', 'C', 'Web Security');
