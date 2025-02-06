# Gradio Quiz Application

This project creates an interactive quiz using the Gradio library. The application covers various topics, evaluates the user's answers, and provides immediate feedback.

---

## **Quiz Topics and Questions**

1. **Quantitative Aptitude**
   - Question: *If a train travels 60 km in 1 hour, how much distance will it cover in 3 hours?*
   - Options: 120 km, 150 km, 180 km, 200 km  
   - **Answer:** 180 km  

2. **Mathematics**
   - Question: *What is the derivative of x²?*  
   - Options: x, 2x, x², 1  
   - **Answer:** 2x  

3. **Computer Science**
   - Question: *Which data structure uses LIFO (Last In First Out) principle?*  
   - Options: Queue, Stack, Array, Linked List  
   - **Answer:** Stack  

4. **Logical Reasoning**
   - Question: *If all cats are animals and some animals are dogs, which of the following is correct?*  
   - Options: All animals are cats, Some dogs are cats, All cats are dogs, Some animals are dogs  
   - **Answer:** Some animals are dogs  

5. **Quantitative Aptitude**
   - Question: *A person buys an item for $100 and sells it for $150. What is the profit percentage?*  
   - Options: 25%, 50%, 75%, 100%  
   - **Answer:** 50%  

---

## **Quiz Evaluation Function**

The `evaluate_quiz()` function processes the user's answers and provides:
- **Score:** Total correct answers.
- **Feedback:** Detailed feedback for each question.

---

## **Gradio Interface Setup**

The `quiz_interface()` function builds the interactive quiz interface using Gradio components:
- **Input:** Radio buttons for each question.
- **Output:** Textbox for score and detailed feedback.

### **Function: evaluate_and_display()**
This function:
- Evaluates user answers.
- Returns the quiz score and detailed feedback.

### **Gradio Components**
- `gr.Radio`: Displays questions with selectable options.
- `gr.Textbox`: Outputs the score and feedback.

---

## **How to Run the Application**
1. Ensure you have Gradio installed:
   ```bash
   pip install gradio
