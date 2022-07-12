class QuizBrain:
    
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def play(self):
        while self.still_has_questions():
            self.next_question()
        else:
            self.end_quiz()
    
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)    
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        if self.check_answer(user_answer, current_question.answer): 
            print("Correct!")
            self.score += 1
        else: print("Incorrect...")
        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n\n")
    
    def check_answer(self, ans : str, corr : str):
        return ans.capitalize() == corr.capitalize()
    
    def end_quiz(self):
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}.")