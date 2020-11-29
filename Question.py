import random
questionbank = []
class Question:
    def __init__(self,answer1,answer2,answer3,answer4,question,rightAnswer):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.question = question
        self.rightAnswer = rightAnswer
        questionbank.append(self)
   
   
    def __str__(self):
        return f"\nA kérdése a következő: {self.question}\n 1. {self.answer1}          2. {self.answer2}\n 3. {self.answer3}         4. {self.answer4}\n"
