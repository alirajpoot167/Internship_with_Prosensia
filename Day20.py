def load_questions():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "Which programming language is this quiz written in?", "answer": "Python"},
        {"question": "What is the largest living species of lizard?", "answer": "Komodo dragon"},
        {"question": "What is the chemical symbol for gold?", "answer": "Au"}
    ]
    return questions

def ask_question(question):
    user_answer = input(question["question"] + " ")
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
        return True
    else:
        print(f"Sorry, that's incorrect. The correct answer is {question['answer']}.")
        return False

def main():
    questions = load_questions()
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
    print(f"Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    main()