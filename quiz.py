import gradio as gr

# List of quiz questions and answers from various topics
quiz_data = [
    # Quantitative Aptitude
    {"question": "If a train travels 60 km in 1 hour, how much distance will it cover in 3 hours?", "options": ["120 km", "150 km", "180 km", "200 km"], "answer": "180 km"},

    # Mathematics
    {"question": "What is the derivative of x^2?", "options": ["x", "2x", "x^2", "1"], "answer": "2x"},

    # Computer Science
    {"question": "Which data structure uses LIFO (Last In First Out) principle?", "options": ["Queue", "Stack", "Array", "Linked List"], "answer": "Stack"},

    # Logical Reasoning
    {"question": "If all cats are animals and some animals are dogs, which of the following is correct?", "options": ["All animals are cats", "Some dogs are cats", "All cats are dogs", "Some animals are dogs"], "answer": "Some animals are dogs"},

    # Quantitative Aptitude
    {"question": "A person buys an item for $100 and sells it for $150. What is the profit percentage?", "options": ["25%", "50%", "75%", "100%"], "answer": "50%"}
]

# Function to evaluate the quiz and provide immediate feedback for each question
def evaluate_quiz(answers):
    score = 0
    total_questions = len(quiz_data)
    feedback = []

    for i, user_answer in enumerate(answers):
        correct_answer = quiz_data[i]["answer"]
        if user_answer == correct_answer:
            score += 1
            feedback.append(f"Question {i + 1}: Correct!")
        else:
            feedback.append(f"Question {i + 1}: Incorrect. Correct answer: {correct_answer}")

    return score, feedback

# Create Gradio interface with immediate feedback for each question
def quiz_interface():
    def evaluate_and_display(*answers):
        score, feedback = evaluate_quiz(answers)
        return f"Your Score: {score}/{len(quiz_data)}", "\n".join(feedback)

    components = []
    for item in quiz_data:
        components.append(gr.Radio(choices=item["options"], label=item["question"]))

    interface = gr.Interface(
        fn=evaluate_and_display,
        inputs=components,
        outputs=[gr.Textbox(label="Score"), gr.Textbox(label="Feedback", lines=10)],
        live=True
    )
    interface.launch()

if __name__ == "__main__":
    quiz_interface()
