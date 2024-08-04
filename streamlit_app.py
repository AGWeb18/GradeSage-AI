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

# Define the subscription URLs
monthly_sub_url = "https://buy.stripe.com/28ocO9fMubQB0EgbII"
annual_sub_url = "https://buy.stripe.com/fZe6pLcAiaMx5YAbIJ"

# Page config
st.set_page_config(page_title="GradeSage AI", page_icon="🎓", layout="wide")

# Custom CSS with improved styling and consistent dark blue theme
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
    }
    .a {
        background-color: #00008B;
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
    /* Unified button styles */
    .stButton > button,
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .cta-button,
    .subscribe-button,
    div[data-testid="stFormSubmitButton"] > button,
    .sidebar .streamlit-button {
        background-color: #00008B !important;  /* Dark Blue */
        color: white !important;
        font-weight: bold !important;
        padding: 0.5rem 1rem !important;
        border-radius: 5px !important;
        border: none !important;
        transition: background-color 0.3s ease !important;
        text-decoration: none;
    }
    /* Unified hover styles */
    .stButton > button:hover,
    .stTextInput > div > div > input:hover,
    .stSelectbox > div > div > select:hover,
    .cta-button:hover,
    .subscribe-button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover,
    .sidebar .streamlit-button:hover {
        background-color: #0000CD !important;  /* Medium Blue */
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #4F4F4F;
    }
    .sidebar .element-container div[data-testid="stMarkdownContainer"] p a {
        background-color: #00008B !important;
    }
    .sidebar .element-container div[data-testid="stMarkdownContainer"] p a:hover {
        background-color: #0000CD !important;
    }
    .sidebar .element-container div[data-testid="stMarkdownContainer"] p a {
        background-color: #00008B !important;
    }
    .sidebar .element-container div[data-testid="stMarkdownContainer"] p a:hover {
        background-color: #0000CD !important;
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

# Custom CSS with more specific selectors and !important flags
st.markdown("""
    <style>
    .sidebar .element-container div[data-testid="stMarkdownContainer"] p a,
    .sidebar .element-container div[data-testid="stMarkdownContainer"] p a div {
        background-color: #00008B !important;
        color: white !important;
        font-weight: bold !important;
        padding: 0.5rem 1rem !important;
        border-radius: 5px !important;
        border: none !important;
        text-align: center !important;
        text-decoration: none !important;
        display: inline-block !important;
        width: 100% !important;
        box-sizing: border-box !important;
        transition: background-color 0.3s ease !important;
    }
    .sidebar .element-container div[data-testid="stMarkdownContainer"] p a:hover,
    .sidebar .element-container div[data-testid="stMarkdownContainer"] p a:hover div {
        background-color: #0000CD !important;
    }
    </style>
    """, unsafe_allow_html=True)

# In your sidebar
with st.sidebar:
    st.title("GradeSage AI")
    
    # Use add_auth for optional authentication
    add_auth(
        required=False,
        login_button_text="Login with Google",
        login_button_color="#00008B",
        login_sidebar=True
    )
    
    # Check if user is logged in
    if 'email' in st.session_state and st.session_state.email:
        st.success(f"Logged in as {st.session_state.email}")
        
        # Check if user is subscribed
        if 'user_subscribed' in st.session_state and st.session_state.user_subscribed:
            st.success("Subscribed user")
        else:
            st.warning("Not subscribed")
    else:
        st.info("Please log in to access all features")

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

    # CTA Button (updated to use the new color scheme)
st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <a href="#" class="cta-button">Start Now</a>
    </div>
    """, unsafe_allow_html=True)


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


st.markdown(f"""
    <style>
    .pricing-table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 2rem;
    }}
    .pricing-table th, .pricing-table td {{
        padding: 1rem;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }}
    .pricing-table th {{
        background-color: #f2f2f2;
    }}
    .check {{
        color: green;
        font-size: 1.2rem;
    }}
    </style>
    <table class="pricing-table">
        <tr>
            <th>Feature</th>
            <th>Monthly Plan</th>
            <th>Annual Plan</th>
        </tr>
        <tr>
            <td>Price</td>
            <td>$15/month</td>
            <td>$150/year ($12.50/month)</td>
        </tr>
        <tr>
            <td>Unlimited Grading</td>
            <td><span class="check">✓</span></td>
            <td><span class="check">✓</span></td>
        </tr>
        <tr>
            <td>24/7 Support</td>
            <td><span class="check">✓</span></td>
            <td><span class="check">✓</span></td>
        </tr>
        <tr>
            <td>Priority Processing</td>
            <td></td>
            <td><span class="check">✓</span></td>
        </tr>
        <tr>
            <td></td>
            <td><a href="{monthly_sub_url}" class="subscribe-button">Subscribe Monthly</a></td>
            <td><a href="{annual_sub_url}" class="subscribe-button">Subscribe Annually</a></td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

st.markdown('<p style="text-align: center; margin-top: 1rem; font-weight: bold;">Cancel Anytime</p>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 GradeSage AI. All rights reserved.</div>', unsafe_allow_html=True)

# File upload and processing (only visible when logged in)
if 'email' in st.session_state and st.session_state.email and 'user_subscribed' in st.session_state and st.session_state.user_subscribed:
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
                                    f"Estimated time re
                                      ing: {(total_wr_questions - processed_questions) * question_time / 60:.2f} minutes")

                # Update progress bar
                progress_bar.progress((i + 1) / total_users)

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
