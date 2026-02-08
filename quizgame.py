questions=("1.  Which planet is closest to the Sun?",
           "2.  Who wrote Romeo and Juliet?",
           "3.  What year did World War II end?",
           "4.  Which planet has the shortest day?",
           "5.  What is the smallest country in the world by land area?",)

options=(("A. Earth","B. Mercury","C. Venus","D. Mars"),
         ("A.  Shake Spere","B. Ayush Shayar","C. Likha hoga kisi ne hmko kya","D. pta ni"),
         ("A. 1988","B. 1987","C. 1989","D. 1990"),
         ("A. mercury","B. Uranus","C. Jupiter","D. Earth"),
         ("A. Nauru","B. Tuvalu","C. San Mario","D. Vatican City")
         )

score=0
question_no=0
guesses=[]
answers=("B","A","C","C","D")

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_no]:
        print(option)
    guess=input("ENTER A OPTION: A  B  C  D:").upper()
    guesses.append(guess)
    if guess==answers[question_no]:
        print("--CORRECT!🥳--")
        score+=1
    else:
        print("--INCORECT!--")
        print(f"correct answwer is {answers[question_no]} you dumb 🤡")
    question_no+=1

print("")
print("---------------------")
print("-------RESULTS-------")
print("---------------------")
print("")
print(f"YOUR SCORE IS {score} OUT OF 5")
accuracy=int(score/len(questions))*100
print(f"YOU ARE {accuracy}% accurate")