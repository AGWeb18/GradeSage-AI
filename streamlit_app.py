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

# Sidebar enhancements
st.sidebar.title("GradeSage AI")

# User authentication status
user_info = add_auth(required=False)

if user_info:
    st.sidebar.success(f"Welcome, {user_info['given_name']}!")
    st.sidebar.button("Logout", key="logout")
else:
    st.sidebar.info("Please log in to access all features.")


# Version info
st.sidebar.write("---")
st.sidebar.write("Version 1.0.0")

# Custom CSS with font color fixes and new carousel styles
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        font-size: 50px !important;
        color: #1E1E1E !important;
        animation: fadeIn 1.5s;
    }
    .subtitle {
        font-size: 25px !important;
        color: #4F4F4F !important;
        animation: slideIn 1.5s;
    }
    p, .stButton > button {
        color: #1E1E1E !important;
    }
    .stTextArea > div > div > textarea {
        color: #1E1E1E !important;
    }
    .example-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .example-title {
        font-size: 20px !important;
        font-weight: bold;
        margin-bottom: 10px;
    }
    @keyframes fadeIn {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    @keyframes slideIn {
        0% {transform: translateY(50%); opacity: 0;}
        100% {transform: translateY(0); opacity: 1;}
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

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<p class="title">GradeSage AI</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Smart grading for all platforms.</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Desire2Learn and beyond.</p>', unsafe_allow_html=True)

    st.write("##")
    st.markdown('<p class="subtitle">📝 Grade short answers/essays in minutes</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🌐 Compatible with any Learning Management System</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🤖 Powered by advanced AI technology</p>', unsafe_allow_html=True)

with col2:
    st_lottie(lottie_book, height=300, key="book")

# Example carousel section
st.write("---")
st.write("## GradeSage AI in Action")

examples = [
    {
        "title": "Example 1: Short Answer Grading",
        "question": "Explain the concept of supply and demand in economics.",
        "answer": "Supply and demand are fundamental economic principles that determine the price and quantity of goods in a market. Supply represents the amount of a product producers are willing to sell at various prices, while demand represents the amount consumers are willing to buy. The point where supply and demand intersect determines the market equilibrium price and quantity.",
        "score": 4,
        "feedback": "Excellent explanation covering the key aspects of supply and demand. Consider adding an example to illustrate the concept further."
    },
    {
        "title": "Example 2: Essay Evaluation",
        "question": "Discuss the impact of social media on modern communication.",
        "answer": "Social media has revolutionized modern communication by providing instant connectivity and global reach. Platforms like Facebook, Twitter, and Instagram have changed how we share information, connect with others, and consume content. While it has improved access to information and facilitated new forms of expression, concerns about privacy, misinformation, and mental health impacts have also arisen.",
        "score": 3,
        "feedback": "Good overview of social media's impact. To improve, provide specific examples and discuss both positive and negative effects in more detail."
    },
    {
        "title": "Example 3: Technical Question Assessment",
        "question": "Describe the process of photosynthesis in plants.",
        "answer": "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to produce oxygen and energy in the form of sugar. It occurs in the chloroplasts, specifically using the green pigment chlorophyll. The process has two stages: light-dependent reactions and light-independent reactions (Calvin cycle).",
        "score": 4,
        "feedback": "Very good explanation of photosynthesis. To achieve a perfect score, include more details about the light-dependent and light-independent reactions."
    }
]

for i, example in enumerate(examples):
    with st.expander(f"{example['title']}"):
        st.markdown(f"<div class='example-card'>", unsafe_allow_html=True)
        st.markdown(f"<p class='example-title'>Question:</p>", unsafe_allow_html=True)
        st.write(example['question'])
        st.markdown(f"<p class='example-title'>Student Answer:</p>", unsafe_allow_html=True)
        st.write(example['answer'])
        st.markdown(f"<p class='example-title'>AI Grading:</p>", unsafe_allow_html=True)
        st.write(f"Score: {example['score']}/5")
        st.write(f"Feedback: {example['feedback']}")
        st.markdown("</div>", unsafe_allow_html=True)

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

<p style="text-align: center; margin-top: 20px; font-weight: bold; color: #4F4F4F;">
    Cancel Anytime
</p>
""", unsafe_allow_html=True)


# Footer
st.write("---")
st.write("© 2024 GradeSage AI. All rights reserved.")
# st.write("Great to see you! Ready to revolutionize your grading process? Subscribe to get started.")    
add_auth(required=True)

st.write("Welcome! Upload your CSV file to grade assignments using AI.")
# File uploader
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

#