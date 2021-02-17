"""Part One"""

class Student(object):
    """A student"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """A question on the exam"""

    def __init__(self, question, correct_answer): 
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Ask a question
        
        Will show the user a question, take in their answer
        and if the answer is correct it will return True
        """

        answer = input(self.question)
        return self.correct_answer == answer 


class Exam(object):
    """An exam"""

    def __init__(self, name):
        self.name = name
        self.questions = []
    
    def add_question(self, question):
        """Add question to exam"""

        self.questions.append(question)

    def administer(self):
        """Administer the test and return the score"""

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return 100 * (float(score) / len(self.questions))
        

