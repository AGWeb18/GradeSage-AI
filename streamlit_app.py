import streamlit as st
import anthropic
import pandas as pd
import numpy as np
import os
import re
import time
import json
import requests 
from st_paywall import add_auth
from streamlit_lottie import st_lottie

# Page config
st.set_page_config(page_title="GradeSage AI", page_icon="🎓", layout="wide")

# Custom CSS with improved styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
    }
    .title {
        font-size: 3.5rem !important;
        color: #1E1E1E !important;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.5rem !important;
        color: #4F4F4F !important;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 2rem !important;
        color: #1E1E1E !important;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .feature-box {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feature-icon {
        font-size: 2rem;
        margin-right: 1rem;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
    }
    .stButton > button {
        background-color: #FF7F50;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #FF6347;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #4F4F4F;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_book = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_1a8dx7zj.json')

# Header
st.markdown('<h1 class="title">GradeSage AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Smart grading for all platforms. Desire2Learn and beyond.</p>', unsafe_allow_html=True)

# Main content area
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown('<h2 class="section-title">Features</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-box">
        <span class="feature-icon">📝</span> Grade short answers/essays in minutes
    </div>
    <div class="feature-box">
        <span class="feature-icon">🌐</span> Compatible with any Learning Management System
    </div>
    <div class="feature-box">
        <span class="feature-icon">🤖</span> Powered by advanced AI technology
    </div>
    """, unsafe_allow_html=True)

with col2:
    st_lottie(lottie_book, height=300, key="book")

# User authentication status and buttons
user_info = add_auth(required=False)


# New Pricing Section
st.write("---")
st.write("## Pricing")

st.markdown("""
<style>
.pricing-container {
    display: flex;
    justify-content: center;
    align-items: stretch;
    gap: 20px;
    margin-top: 30px;
}
.pricing-card {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 30px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.3s ease;
    
}
.pricing-card:hover {
    transform: translateY(-5px);
}
.pricing-title {
    font-size: 24px;
    color: white;
    font-weight: bold;
    margin-bottom: 20px;
    color: #1E1E1E;
}
.pricing-price {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #4F4F4F;
}
.pricing-details {
    margin-bottom: 20px;
    color: #4F4F4F;
}
.pricing-cta {
    background-color: #F63366;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
.pricing-cta:hover {
    background-color: #D81B60;
}
</style>

<div class="pricing-container">
    <div class="pricing-card">
        <div>
            <h3 class="pricing-title">Monthly Plan</h3>
            <p class="pricing-price">$15/month</p>
            <p class="pricing-details">Perfect for short-term projects or to try out our service.</p>
        </div>
        <a href="#" class="pricing-cta">Get Started</a>
    </div>
    <div class="pricing-card">
        <div>
            <h3 class="pricing-title">Annual Plan</h3>
            <p class="pricing-price">$150/year</p>
            <p class="pricing-details">Save $30 with our annual plan. Best value for regular use.</p>
        </div>
        <a href="#" class="pricing-cta">Get Started</a>
    </div>
</div>

""", unsafe_allow_html=True)

st.markdown('<p style="text-align: center; margin-top: 1rem; font-weight: bold;">Cancel Anytime</p>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 GradeSage AI. All rights reserved.</div>', unsafe_allow_html=True)

# File upload and processing (only visible when logged in)
if user_info:
    st.markdown('<h2 class="section-title">Grade Assignments</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        st.subheader("Column Selection")
        username_col = st.selectbox("Select the username column", df.columns)
        question_type_col = st.selectbox("Select the question type column", df.columns)
        question_col = st.selectbox("Select the question column", df.columns)
        answer_col = st.selectbox("Select the answer column", df.columns)
        mc_score_col = st.selectbox("Select the multiple-choice score column", df.columns)

        # Add a user input for the maximum score
        max_score = st.number_input("Enter the maximum score:", min_value=1, value=25, step=1)

        # Add a button to run the script
        if st.button("Run Grading"):
            st.write("Processing your file...")

            pd.set_option("display.max_columns", None)

            client = anthropic.Anthropic(
                api_key=os.getenv("ANTHROPIC_API_KEY"),
            )

            def safe_extract_number(string):
                try:
                    first_four = string[:4]
                    digits = re.findall(r'\d', first_four)
                    return int(''.join(digits)) if digits else 0
                except:
                    return 0

            def extract_score_and_comment(response):
                try:
                    # Check if the response is a TextBlock object
                    if hasattr(response, 'text'):
                        content = response.text
                    else:
                        content = str(response)

                    # Find the first digit in the string
                    match = re.search(r'\d', content)
                    if match:
                        score_start = match.start()
                        score_end = content.find('|', score_start)
                        if score_end != -1:
                            score = int(content[score_start:score_end])
                            comment = content[score_end + 1:].strip()
                            return score, comment
                    return 0, content  # Return the whole content as a comment if no score is found
                except Exception as e:
                    print(f"Error extracting score and comment: {str(e)}")
                    return 0, str(content)  # Return the whole content as a string in case of any error


                
            def get_teaching_assistant_score(student_question, student_answer):
                try:
                    message = client.messages.create(
                        model="claude-3-5-sonnet-20240620",
                        max_tokens=618,
                        temperature=0,
                        system="""You are a Teaching Assistant at a university level, responsible for evaluating student responses across various courses. 
                        
                        Your task is to read the provided question and student answer, then assess the response quality on a scale of 0 to 5.

                        Scoring guidelines:
                        0 - No answer provided or completely blank response
                        1 - Nonsensical answer or completely incorrect/irrelevant response
                        2 - Partially correct but significant misunderstandings present
                        3 - Mostly correct with minor errors or omissions
                        4 - Correct answer with good understanding demonstrated
                        5 - Excellent answer showing comprehensive understanding and insight

                        Please provide your evaluation in the following pipe-delimited format:
                        SCORE|COMMENT

                        The SCORE should be a single digit from 0 to 5.
                        The COMMENT should provide a brief explanation of your scoring decision, highlighting strengths or areas for improvement in the student's response.

                        Example output:
                        4|The answer demonstrates a strong grasp of the concept with minor details missing.

                        Evaluate the student's response thoughtfully and provide constructive feedback.""",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": f"Question: {student_question}?\nAnswer: {student_answer}"
                                    }
                                ]
                            }
                        ]
                    )
                    return message.content[0].text

                
                except Exception as e:
                    st.error(f"Error in API call: {str(e)}")
                    return "0|Error in API call"

            l_responses = []

            # Create a progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            details_text = st.empty()

            total_users = len(df[username_col].unique())
            total_wr_questions = len(df[df[question_type_col] == 'WR'])

            start_time = time.time()
            processed_questions = 0

            for i, user_name in enumerate(df[username_col].unique()):
                user_start_time = time.time()
                status_text.text(f"Processing user {i+1} of {total_users}: {user_name}")

                user_df = df[df[username_col] == user_name]
                
                # Process MC questions
                mc_df = user_df[user_df[question_type_col] == 'MC']
                mc_score = mc_df[mc_score_col].sum()  # Sum of MC scores for the user
                
                # Process WR questions
                wr_df = user_df[user_df[question_type_col] == 'WR']
                user_wr_questions = len(wr_df)
                
                for j, (_, row) in enumerate(wr_df.iterrows()):
                    question_start_time = time.time()
                    response = get_teaching_assistant_score(row[question_col], row[answer_col])
                    ai_score, ai_comment = extract_score_and_comment(response)
                    l_responses.append([user_name, mc_score, row[question_col], row[answer_col], ai_score, ai_comment])
                    processed_questions += 1
                    question_time = time.time() - question_start_time
                    
                    details_text.text(f"User {i+1}/{total_users}, WR Question {j+1}/{user_wr_questions}\n"
                                    f"Total progress: {processed_questions}/{total_wr_questions} WR questions\n"
                                    f"Time for last question: {question_time:.2f}s\n"
                                    f"Estimated time remaining: {(total_wr_questions - processed_questions) * question_time / 60:.2f} minutes")

                # Update progress bar
                progress_bar.progress((i + 1) / total_users)
                
                user_time = time.time() - user_start_time
                st.write(f"Completed user {user_name} in {user_time:.2f} seconds")

            # After the loop
            responses_df = pd.DataFrame(l_responses, columns=['Student', 'MC-Score', 'Question', 'Answer', 'AI-Score', 'AI-Comment'])
            # Ensure all columns are of the correct type
            responses_df['AI-Score'] = pd.to_numeric(responses_df['AI-Score'], errors='coerce').fillna(0).astype(int)
            responses_df['AI-Comment'] = responses_df['AI-Comment'].astype(str)
            # The rest of the processing remains largely the same
            summary_df = responses_df.groupby('Student').agg({
                'MC-Score': 'max',
                'AI-Score': 'sum'
            }).reset_index()

            # Calculate total score
            summary_df['Total w Bellcurve'] = summary_df['MC-Score'] + summary_df['AI-Score']

            # Calculate score out of the user-specified maximum
            max_total = summary_df['Total w Bellcurve'].max()
            summary_df[f'Score out of {max_score}'] = (summary_df['Total w Bellcurve'] / max_total) * max_score

            # Rename columns to match desired output
            summary_df.columns = ['Student', 'Max of MC-Score', 'Sum of AI-Score', 'Total w Bellcurve', f'Score out of {max_score}']

            # Display the summary dataframe
            st.write("Summary of Scores:")
            st.dataframe(summary_df)

            # Create a download button for the summary CSV
            summary_csv = summary_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Summary as CSV",
                data=summary_csv,
                file_name="student_scores_summary.csv",
                mime="text/csv",
            )

            # Display the pivot table-like summary
            st.write("Pivot Table Summary:")
            pivot_summary = summary_df.describe()
            st.dataframe(pivot_summary)

            # Create a download button for the pivot summary CSV
            pivot_csv = pivot_summary.to_csv(index=True).encode('utf-8')
            st.download_button(
                label="Download Pivot Summary as CSV",
                data=pivot_csv,
                file_name="student_scores_pivot_summary.csv",
                mime="text/csv",
            )

            # Display detailed results
            st.write("Detailed Results:")
            st.dataframe(responses_df)

            # Download button for detailed CSV
            detailed_csv = responses_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Detailed Results as CSV",
                data=detailed_csv,
                file_name="student_detailed_results.csv",
                mime="text/csv",
            )

            # Add this new section to identify and display the worst-performing question
            st.subheader("Worst-Performing Question")

            # Group by Question and calculate the average AI-Score
            question_scores = responses_df.groupby('Question')['AI-Score'].mean().reset_index()

            # Identify the worst-performing question
            worst_question = question_scores.loc[question_scores['AI-Score'].idxmin()]

            # Display the worst-performing question in a sentence
            st.write(f"The question students struggled with the most is:")
            st.markdown(f"**{worst_question['Question']}**")
            st.write(f"Average score: {worst_question['AI-Score']:.2f} out of 5")
