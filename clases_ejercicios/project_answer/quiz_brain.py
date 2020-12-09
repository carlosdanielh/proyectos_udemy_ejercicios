class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.size_list_question = len(question_list)

    def still_has_question(self):
        return self.question_number < self.size_list_question
        
    def next_question(self):
        # if self.question_number < self.size_list_question:
        index = self.question_number
        number = index + 1
        the_question = self.question_list[index].text
        self.question = input(f'Q.{number}: {the_question} (True\\False?): ')
        self.question_number += 1
