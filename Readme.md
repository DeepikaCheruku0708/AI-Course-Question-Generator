# AI Course Question Generator

## Overview

AI Course Question Generator is a Generative AI-powered learning assistant built using Python, Streamlit, and Google's Gemini API.

The application helps students learn technical subjects by generating course-specific questions, answers, important concepts, and interview preparation material. Users can also ask their own questions and receive detailed AI-generated explanations.

---

## Features

### Course-wise Question Generation

Generate learning questions for:

* Python
* Java
* SQL
* Artificial Intelligence
* Machine Learning
* Deep Learning
* NLP
* Generative AI
* Agentic AI
* Prompt Engineering
* DataScience
* Data Engineer
* Git & GitHub
* Linux

### Difficulty Levels

Choose:

* Beginner
* Intermediate
* Advanced

### AI Tutor Mode

Ask any course-related question and receive:

* Simple Explanation
* Detailed Explanation
* Example
* Key Points

### Interview Preparation

Generate course-specific interview questions and answers.

---

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* Python Dotenv
* Git
* GitHub

---

## Project Structure

AI-Course-Question-Generator/

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

└── .env (Local Only)

---

## Installation

### Clone Repository

```bash
git clone https://github.com/DeepikaCheruku0708/AI-Course-Question-Generator.git
```

### Navigate to Project Folder

```bash
cd AI-Course-Question-Generator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Do not upload the `.env` file to GitHub.

---

## Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## How It Works

### Question Generator

1. Select a course.
2. Select difficulty level.
3. Click Generate Questions.
4. AI creates:

   * Questions
   * Answers
   * Important Concepts
   * Interview Questions

### AI Tutor

1. Select a course.
2. Enter your question.
3. Click Get Answer.
4. AI provides:

   * Simple Explanation
   * Detailed Explanation
   * Example
   * Key Points

---

## Sample Use Cases

### SQL

Question:

```text
What is a Primary Key?
```

### Python

Question:

```text
What is List Comprehension?
```

### Machine Learning

Question:

```text
What is Overfitting?
```

---

## Learning Outcomes

This project helped me learn:

* Python Programming
* Streamlit Application Development
* Prompt Engineering
* Gemini API Integration
* Environment Variables
* Git & GitHub
* Generative AI Applications

---


## Author

Deepika Cheruku


---

## Disclaimer

This project is developed for educational and learning purposes. API keys and sensitive credentials are excluded from the repository using `.gitignore`.
