# This Python file uses the following encoding: utf-8                         Forrás: https://www.python.org/dev/peps/pep-0263/
import question_giver
import Question
import random
questionNumber = 1
f = open("Questions.txt", "r",encoding="utf-8")         #https://stackoverflow.com/questions/12330522/how-to-read-a-file-without-newlines
temp = f.read().splitlines()                            #
for x in temp:
    pieces = x.split(",")
    print(pieces)
    Question.Question(pieces[0],pieces[1],pieces[2],pieces[3],pieces[4],pieces[5])

question_giver.clear()
input("Üdv A legyen ön is Kalkulustában, a játékban 10 kérdésre kell majd helyes választ adnod.\n1 életed van tehát ha elrontasz egy kérdést akkor a játék véget ér.\nMinden kérdésre 4 lehetséges választ fogsz kapni és a szerinted helyesnek ítélt válaszlehetőség sorszámát kell majd beírnod pont nélkül.(pl.: 1).\nMinden jó válaszért 300*(Ahanyadik kérdés) pontot kapsz.\nA játék végén láthatod,hogy mennyi pontot szereztél és hogy mit rontottál el (ha rontottál el).\nJó játékot és sok pontot!\n\nA játék megkezdéséhez nyomd meg az entert.")
question_giver.clear()
question_giver.next_question(questionNumber)

