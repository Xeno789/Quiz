
import Question
import random
import os
recap = []
score = 0
clear = lambda: os.system('cls')   # https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def next_question(questionLineNumber):
        global score
        questionNumber = random.randint(0,len(Question.questionbank)-1)
        print(Question.questionbank[questionNumber])
        try:
            answer = int(input("Kérlek írd be a helyesnek vélt válasz sorszámát(pont nélkül):"))
        except ValueError:
            print(f"Felvoltam készülve hogy nem számot adsz meg a játéknak vége a(z) {questionLineNumber}. szinten")
            print("Összefoglaló.")
            for x in recap:
                print(x)
            print(f"Összesen:{score}pontot ért el.")
            return
        if answer != 1 and answer != 2 and answer != 3 and answer != 4:
            print("Hibás input(Biztosan csak a sorszámát adta meg a jó válasznak?)")
            try:
                answer = int(input("Próbálja meg újra.(Nincs több second chance)"))
            except ValueError:
                print(f"Szóval csak erre ment ki a játék, hogy lehalok-e. Hát nem!.A játék véget ért a(z) {questionLineNumber}. szinten")
                print("Összefoglaló.")
                for x in recap:
                    print(x)
                print(f"Összesen:{score}pontot ért el.")
                return
            if answer != 1 and answer != 2 and answer != 3 and answer != 4:
                print("Többszöri helytelen input megadása miatt felfüggesztem a játékból.")
                print("Összefoglaló.")
                for x in recap:
                    print(x)
                print(f"Összesen:{score}pontot ért el.")
                return False
        if answer == 1:
            answer = Question.questionbank[questionNumber].answer1
        if answer == 2:
            answer = Question.questionbank[questionNumber].answer2
        if answer == 3:
            answer = Question.questionbank[questionNumber].answer3
        if answer == 4:
            answer = Question.questionbank[questionNumber].answer4
        if str(Question.questionbank[questionNumber].rightAnswer) == str(answer):
            questionLineNumber = questionLineNumber+1
            if questionLineNumber == 11:
                clear()
                score = score+300*(questionLineNumber-1)
                print("Gratulálok sikeresen kivitted a játékot")
                print(f"Összesen:{score} pontot értél el.Gratulálok hozzá!")
                input("Nyomj entert a válaszaid megtekintéséhez.")
                recap.append(f"{questionLineNumber-1}.{Question.questionbank[questionNumber].question}-re a(z) {answer} Helyes válasz volt.")
                print("Itt megtekintheted a kérdéseket amiket megválaszoltál.")
                for x in recap:
                    print(x)
                input("Nyomd meg az entert a kilépéshez.\n")
                return
            score = score+300*(questionLineNumber-1)
            recap.append(f"{questionLineNumber-1}.{Question.questionbank[questionNumber].question}-re a(z) {answer} Helyes válasz volt.")
            print(f"\nA válaszod helyes volt,Összesen: {score} pontod van jelenleg.\n")
            input(f"Nyomj egy entert,hogy továbblépj a {questionLineNumber}. szintre\n")
            clear()
            Question.questionbank.pop(questionNumber)
            next_question(questionLineNumber)
        else:
            print("\nA válaszod helytelen volt,Köszönöm hogy kipróbáltad a játékom\n")
            recap.append(f"{questionLineNumber}.{Question.questionbank[questionNumber].question} Helytelen válasz volt, a válaszod:{answer} a helyes válasz a {Question.questionbank[questionNumber].rightAnswer} lett volna.")
            print("Összefoglaló.")
            for x in recap:
                print(x)
            print(f"Összesen:{score} pontot ért el.Gratulálok hozzá!")
            input("Nyomj entert a kilépéshez.")
            return
