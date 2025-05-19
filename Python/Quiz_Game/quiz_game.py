import streamlit as st

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": "JavaScript"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    }
]

# Streamlit app
st.title("Quiz Game")

# Initialize session state for score and question index
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# Display the current question
if st.session_state.question_index < len(quiz_data):
    current_question = quiz_data[st.session_state.question_index]
    st.subheader(current_question["question"])
    user_answer = st.radio("Choose your answer:", current_question["options"])

    if st.button("Submit"):
        if user_answer == current_question["answer"]:
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is {current_question['answer']}.")

        st.session_state.question_index += 1
        # st.query_params() is not callable; removed or replaced with appropriate logic if needed
else:
    st.write(f"Quiz completed! Your final score is {st.session_state.score}/{len(quiz_data)}.")
    if st.button("Restart"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        # st.experimental_rerun()