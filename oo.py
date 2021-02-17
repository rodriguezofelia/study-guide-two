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
        

class StudentExam(object):
    """Stores student's name, exam and score for the exam"""

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None
    
    def take_test(self):
        """Administers exam and assigns score to student"""

        self.score = self.exam.administer()

        print(f'The score is {self.score}')

def example():
    exam = Exam('midterm')

    tuple_q = Question("Once tuples are created, they can't be what?", "changed")

    exam.add_question(tuple_q)

    set_q = Question("What will return a new set with only elements that present in both sets?", "intersection")

    exam.add_question(set_q)

    dict_q = Question("What dictionary method will get a key value pair in a tuple format?", ".items()")

    exam.add_question(dict_q)

    student = Student("Larry", "Barry", "123 Main Street, Austin, TX")

    larrys_midterm = StudentExam(student, exam)

    larrys_midterm.take_test()

example()