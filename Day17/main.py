from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    """Adds objects to an empty list"""
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

# for question_number in question_bank:
#     number = 0
#     question_pool = QuizBrain(question_number.text,number)
#     ask_question = question_pool.next_question(question_number.text, question_number.answer)





# print(question_bank)
#Access the text and answer from the objects in a list.
# print(question_bank[0].text)
# print(question_bank[0].answer)
