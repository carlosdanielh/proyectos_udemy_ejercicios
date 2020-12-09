from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

size_list_question_data = len(question_data)
question_bank = []

for question in question_data:
    text_question = question['text']
    answer_question = question['answer']
    each_question = Question(text_question, answer_question)
    question_bank.append(each_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print('you finish the game')
print(f'total score {quiz.score}/{quiz.question_number}')
