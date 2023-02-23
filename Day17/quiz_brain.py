#Ask Question
#Checking if the answer is correct
#Checking if we're at the end of a quiz

class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.questions_list = q_list
        #print(questions_list)
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
        # This is what I originally wrote:
        # if self.question_number != 12:
        #     return True
        # else:
        #     return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} {current_question.text} (True/False)? ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer.lower()}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
    # I started with this:
    # def next_question(self,q_list, questions_answer):
    #     user_answers = input(f"Q {q_list} (True/False)? ")
    #     if questions_answer == user_answers:
    #         self.question_number += 1
    #         # user_score += 1
    #         print("You got it right!")
    #         print(f"The correct answer was: {questions_answer}")
    #         print(f"Your current question numer is {self.question_number}")
    #     else:
    #         self.question_number += 1
    #         #user_score += 0
    #         print("You got it wrong!")
    #         print(f"The correct answer was: {questions_answer}")
    #         print(f"Your current question number is {self.question_number}")

