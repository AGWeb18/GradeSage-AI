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
from PIL import Image

# Grade Sage Logo
logo = Image.open("GradeSageLogo.png")  # Adjust the path if necessary

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
    .hero {
        text-align: center;
        padding: 3rem;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        
    }
    .hero:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}
    .title {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        font-weight: bold;
        color: #1E1E1E;
    }

    .subtitle {
        font-size: 1.8rem;
        margin-bottom: 1rem;
        color: #4F4F4F;
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
        transition: transform 0.3s ease;
    }
    .feature-box:hover {
        transform: translateY(-5px);
    }
    .feature-icon {
        font-size: 2rem;
        margin-right: 1rem;
        color: #00008B;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
    }
    .cta-button {
        background-color: #00008B !important;
        color: white !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 1.2rem !important;
        border-radius: 5px !important;
        text-decoration: none !important;
        transition: background-color 0.3s ease !important;
    }
    .cta-button:hover {
        background-color: #0000CD !important;
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
    .content-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-top: 2rem;
    }
    .features-column {
        flex: 3;
        margin-right: 2rem;
    }
    .lottie-column {
        flex: 2;
    }
</style>
    """, unsafe_allow_html=True)

# Function to load Lottie animation
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return r.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading Lottie animation from {url}: {str(e)}")
        return None

# Load Lottie animation
lottie_book = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_1a8dx7zj.json')

# Sidebar
with st.sidebar:
    st.image(logo, width=150, caption="Secure Grading. Superior Insights.")
    st.markdown("<h1>GradeSage AI</h1>", unsafe_allow_html=True)
    
    add_auth(
        required=False,
        login_button_text="Login with Google",
        login_button_color="#00008B",
        login_sidebar=True
    )
    
    if 'email' in st.session_state and st.session_state.email:
        st.success(f"Logged in as {st.session_state.email}")
        if 'user_subscribed' in st.session_state and st.session_state.user_subscribed:
            st.success("Subscribed user")
        else:
            st.warning("Not subscribed")
    else:
        st.info("Please log in to access all features")

#Main Content
# Determine button behavior based on user status
if 'email' not in st.session_state or not st.session_state.email:
    # User is not logged in
    start_now_url = "https://your-login-url.com"  # Replace with your actual login URL
    button_text = "Login to Start"
elif 'user_subscribed' not in st.session_state or not st.session_state.user_subscribed:
    # User is logged in but hasn't paid
    start_now_url = monthly_sub_url
    button_text = "Subscribe to Start"
else:
    # User is logged in and has paid
    start_now_url = "#grading-section"
    button_text = "Start Grading"

# Use the determined URL and text for the button
st.markdown(f"""
<div class="hero">
    <h1 class="title">🎓 Grade Sage AI 🤖</h1>
    <p class="subtitle">Revolutionize Your Grading Process</p>
    <p class="description">Smart grading for all platforms. From Desire2Learn to Canvas and beyond.</p>
    <div class="features">
        <p>⚡️ Lightning-fast grading</p>
        <p>🎯 Precise feedback</p>
        <p>🌐 Multi-platform compatibility</p>
    </div>
    <a href="{start_now_url}" class="cta-button">{button_text} 🚀</a>
</div>
""", unsafe_allow_html=True)

# Features section
st.markdown("<h2 class='section-title'>Features</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="features-grid">
        <div class="feature-box">
            <span class="feature-icon">📝</span> Grade short answers/essays in minutes
        </div>
        <div class="feature-box">
            <span class="feature-icon">🌐</span> Compatible with any Learning Management System
        </div>
        <div class="feature-box">
            <span class="feature-icon">🤖</span> Powered by advanced AI technology
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st_lottie(lottie_book, height=350, key="book")

# TODO: Improve this section with 3 cards and LOTTIE animations to make it interesting. 
# How it works section
st.markdown("""
    <style>
    .how-it-works-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 20px;
    }
    .how-it-works-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
        width: calc(50% - 10px);
    }
    .how-it-works-card:last-child {
        width: 100%;
    }
    .how-it-works-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 15px;
        text-align: center;
    }
    .lottie-container {
        width: 100%;
        height: 150px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .cta-button {
        background-color: #00008B;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h2 class='section-title'>How It Works</h2>", unsafe_allow_html=True)

# Load Lottie animations
upload_animation = load_lottieurl('https://lottie.host/5d43c250-744b-4378-8131-215f23705caf/F55WqcVsga.json')
analyze_animation = load_lottieurl('https://lottie.host/a2d58474-53d2-448a-9c26-9f01a3ef3868/p4rWDOqsAv.json')
results_animation = load_lottieurl('https://lottie.host/d19d0192-5312-48c3-b169-5a4143dbcb14/KcdG1iIq2O.json')

# Create a container for the cards
with st.container():
    st.markdown('<div class="how-it-works-container">', unsafe_allow_html=True)

    # First two cards
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<h3 class="how-it-works-title">1. Upload Assignments</h3>', unsafe_allow_html=True)
        st_lottie(upload_animation, height=150, key="upload")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<h3 class="how-it-works-title">2. AI Analyzes and Grades</h3>', unsafe_allow_html=True)
        st_lottie(analyze_animation, height=150, key="analyze")
        st.markdown('</div>', unsafe_allow_html=True)

    # Third card (full width)
    st.markdown('<h3 class="how-it-works-title">3. Review and Download Results</h3>', unsafe_allow_html=True)
    st_lottie(results_animation, height=250, key="results")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # CTA button
    if 'email' in st.session_state and st.session_state.email:
        start_now_url = "#grading-section"  # Replace with the actual section URL
        button_text = "Start Grading"
    else:
        start_now_url = "https://buy.stripe.com/fZe6pLcAiaMx5YAbIJ"
        button_text = "Start Now"

    st.markdown(f"""
    <div class="button-container">
        <a href="{start_now_url}" class="cta-button">{button_text}</a>
    </div>
    """, unsafe_allow_html=True)

# Example carousel section
st.write("---")
st.write("## GradeSage AI in Action")

examples = [
    {
        "title": "Example 1: Low Score - Historical Analysis",
        "question": "Analyze the causes of the French Revolution.",
        "answer": "The French Revolution happened because people were unhappy. There was a king and he was bad. People wanted more freedom.",
        "score": 1,
        "feedback": "This answer lacks depth and specific historical details. To improve, include key events, social and economic factors, and the role of Enlightenment ideas. Mention specific figures, dates, and societal conditions that led to the revolution."
    },
    {
        "title": "Example 2: Medium Score - Scientific Explanation",
        "question": "Explain the process of natural selection in evolution.",
        "answer": "Natural selection is a key mechanism of evolution proposed by Charles Darwin. It's the process where organisms with favorable traits are more likely to survive and reproduce, passing these traits to their offspring. This leads to changes in populations over time. Organisms that are better adapted to their environment have a higher chance of survival.",
        "score": 3,
        "feedback": "Good basic explanation of natural selection. To improve, include specific examples of natural selection in action, discuss the role of genetic variation, and explain how this process leads to speciation over time. Consider mentioning concepts like fitness and adaptation in more detail."
    },
    {
        "title": "Example 3: Perfect Score - Literary Analysis",
        "question": "Discuss the theme of ambition in Shakespeare's 'Macbeth'.",
        "answer": "In 'Macbeth', Shakespeare expertly explores the theme of ambition and its corrupting influence. The play portrays ambition as a dangerous force that, when unchecked, can lead to moral decay and ultimately, destruction. Macbeth's ambition, initially sparked by the witches' prophecies, is further fueled by Lady Macbeth's manipulation. This ambition drives him to commit regicide, betraying his king, friend, and moral code. As the play progresses, Macbeth's ambition consumes him, leading to paranoia and more murders to secure his ill-gotten position. Shakespeare juxtaposes Macbeth's destructive ambition with Banquo's more measured approach, highlighting the potential for ambition to be either a virtue or a vice. The tragic conclusion of the play serves as a cautionary tale about the dangers of allowing ambition to override moral considerations and loyalty. Through vivid imagery, soliloquies, and the gradual deterioration of Macbeth's character, Shakespeare masterfully illustrates how unchecked ambition can corrode the soul and lead to one's downfall.",
        "score": 5,
        "feedback": "Excellent analysis! Your response demonstrates a deep understanding of the play's central theme. You've effectively discussed how ambition drives the plot, affects character development, and contributes to the tragic elements of the play. Your comparison between Macbeth and Banquo adds depth to the analysis. Well done!"
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
    # CTA Button (updated to use the new color scheme)

# Pricing Section
st.write("---")
st.write("## Pricing")

# Updated CSS for the pricing table and buttons
st.markdown("""
<style>
.pricing-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 2rem;
}
.pricing-table th, .pricing-table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
.pricing-table th {
    background-color: #f2f2f2;
}
.check {
    color: green;
    font-size: 1.2rem;
}
.subscribe-button {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #00008B;
    color: white;
    text-align: center;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
.subscribe-button:hover {
    background-color: #0000CD;
}
</style>
""", unsafe_allow_html=True)

# Pricing table HTML with button-style links
st.markdown(f"""
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
        <td><a href="{monthly_sub_url}" class="subscribe-button" style="color:white;">Subscribe Monthly</a></td>
        <td><a href="{annual_sub_url}" class="subscribe-button" style="color:white;">Subscribe Annually</a></td>
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
                    content = response.text if hasattr(response, 'text') else str(response)
                    match = re.search(r'\d', content)
                    if match:
                        score_start = match.start()
                        score_end = content.find('|', score_start)
                        if score_end != -1:
                            score = int(content[score_start:score_end])
                            comment = content[score_end + 1:].strip()
                            return score, comment
                    return 0, content
                except Exception as e:
                    print(f"Error extracting score and comment: {str(e)}")
                    return 0, str(content)

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
