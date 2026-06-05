import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


st.title("AI Course Question Generator")

st.write(
    "Generate Questions and Answers for Learning"
)

course = st.selectbox(
    "Select Course",
    [
        "Python",
        "Java",
        "SQL",
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Generative AI",
        "Agentic AI",
        "Prompt Engineering",
        "DataScience",
        "Data Engineer",
        "Git & GitHub",
        "Linix"

    ]
)

level = st.selectbox(
    "Select Difficulty Level",
    [
        "Easy",
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

if st.button("Generate Questions"):

    prompt = f"""
    Generate learning questions and answers.

    Course: {course}

    Difficulty Level: {level}

    Provide:

    1. 20 Questions
    2. Detailed Answers
    3. Important Concepts
    4. Common Interview Questions
    5. Interview Tips

    Format properly with headings.
    """

    with st.spinner("Generating..."):

        response = model.generate_content(prompt)

        st.subheader("Generated Questions")

        st.write(response.text)
        
        st.subheader("Ask Your Own Question")

user_question = st.text_area(
    "Type your question here"
)
       
if st.button("Get Answer"):

    prompt = f"""
    You are an expert tutor.

    Course: {course}

    Student Question:
    {user_question}

    Provide:

    1. Simple Explanation
    2. Detailed Explanation
    3. Example
    4. Key Points

    Explain in beginner-friendly language.
    """

    response = model.generate_content(prompt)

    st.subheader("Answer")

    st.write(response.text)