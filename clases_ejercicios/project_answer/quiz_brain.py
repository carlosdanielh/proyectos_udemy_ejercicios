class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.size_list_question = len(question_list)
        self.score = 0

    def still_has_question(self):
        return self.question_number < self.size_list_question

    def next_question(self):
        # if self.question_number < self.size_list_question:
        index = self.question_number
        number = index + 1
        the_question = self.question_list[index].text
        the_answer = self.question_list[index].answer
        user_answer = input(f'Q.{number}: {the_question} (True\\False?): ')
        self.check_answer(user_answer, the_answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('you\'re wrong!!!')
            print('bay')            

        print(f'the correct answer {correct_answer}')
        print(f'Your current score is: {self.score}/'
              f'{self.question_number + 1}')
