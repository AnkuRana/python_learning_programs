class QuizBrain:

    def __init__(self, question_bank_data):
        self.question_no = 0
        self.question_list = question_bank_data
        self.score = 0

    def still_has_question(self):
        """return True if there are still question left or False"""
        return self.question_no < len(self.question_list)

    def next_question(self):
        """ask Next question to the user and get user input"""
        ask_question = self.question_list[self.question_no].question
        correct_answer = self.question_list[self.question_no].answer
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {ask_question} (True/False): ").lower()
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("You are wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your Score : {self.score}\n")



