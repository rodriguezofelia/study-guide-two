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

class Exam(object):
    """An exam"""

    def __init__(self, name)
        self.name = name
        self.question = []
    
    def add_question(self, question):
        """Add question to exam"""
        self.question.append(question)
