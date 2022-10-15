from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []


def create_question_bank(var_ques, var_answer):
    question_bank.append(Question(var_ques, var_answer))


# Create question Bank with the data available in data
for data in question_data:
    create_question_bank(data['text'], data['answer'])

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You have completed the quiz! Your final score: {quiz.score}/ {quiz.question_no}")
