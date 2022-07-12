from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def init_questions():
    """_summary_

    Returns:
        _type_: _description_
    """
    question_list = []
    for question in question_data:
        question_list.append(Question(question['text'], question['answer']))
    return question_list

def main():
    questions = init_questions()
    quiz = QuizBrain(questions)
    quiz.play()

    
if __name__ == "__main__":
    main()