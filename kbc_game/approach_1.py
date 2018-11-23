from questionsArray import questionsArray              #Getting Array of questions from the external file,check format there
import os
import random


score = 0                                               # incearses on every correct answer
q_no = 0                                                # current question
playerName=""                                           # current User
parawMoney =0                                           # Money to pay if user quits, it depands on which paraw or level he was on

def clear():                                            # Function to clear console and print the score at top
    os.system('cls')
    print("\n"+"your current score is "+str(score)+"\n")

def increaseScore(question_index):                      #Increases score at every correct answer
    global score
    if question_index==10:
        score = score + 100
    elif question_index >=5:
        score = score + 50
    else:
        score = score +10

def parawMoneySetter(p_q_no):                                            #Sets Money to pay if user quits
    global parawMoney
    if p_q_no == 3:
        parawMoney = score
    elif p_q_no == 7:
        parawMoney = score

def initiateQuit():
    print("   "+playerName+" ji ke liye bohot bohot Taliya \n")
    print("   jese ki aapne quit kiya hai toh \n   aap aapni abb tak ki jeeti hui dhan raashi le jaa sakte hai")
    print("   poore "+str(score)+" rupaye")
    exit()

def looseGame():
    print("Afsos "+playerName+", ji aapka jawaab galat hai\n")
    print("Aap ke paraw ke mutabik aapko milte hai : " + str(parawMoney))
    exit();

def askAndRemoveQuestion():
    clear()
    question = questionsArray[random.randrange(len(questionsArray))]
    q_index = questionsArray.index(question)
    print("Q no:"+str(q_no)+" =>"+question["question"]+"\n")
    for option,i in zip(question["options"],range(4)):
        print(str(i)+" : "+str(option)+"\n")
    print("5 for Quiting")
    userAnswer = int(input("choose your answer"+"\n"))
    if userAnswer==question["correct"]:
        increaseScore(q_no)
        parawMoneySetter(q_no)
        print("well played "+playerName+", ji aapki dhan rasi badh ke ho gayi hai :"+str(score)+"\n")
        input("press <ENTER key> for next question")
        questionsArray.pop(q_index)
        clear()
    elif userAnswer == 5:
        initiateQuit()
    else:
        looseGame()



def initialize_Game():                                  #talking about rules of game
    global playerName
    clear()
    playerName = str(input("kripya aapka naam bataye \n"))
    clear()
    print(" => Iss game me 10 sawal hai: \n")
    print(" => pehle 4 sawal aapko 10 Rupaye ki barhat dilayenge \n")
    print(" => 5-9 tak aap har sawal par payenge 50 Rupaye \n")
    print(" => akhiri sawal par aapko milenge 100 Rupaye \n")
    input(" => press <ENTER key> to continue")
    clear()
    print(" => Khel me 2 paraw hai: parsn 3 ,7 aur 10  par \n")
    print(" => yadi aap parsn 1 se 4 ke beech haarte \n    hai toh aap sirf 30 Rs le jayenge \n")
    print(" => aur 3 se 7 ke beech haarne par bas 340 rs \n")
    print(" => Quit karne ki sthiti me aap aapni \n    poori jeeti hui dhan rashi \n    le jaa sakte hai \n")
    input(" => press <ENTER key> to continue")
    clear()

def runGame():
    global q_no
    initialize_Game()
    while q_no < 10:
        q_no = q_no + 1
        askAndRemoveQuestion()
    clear()
    print("MUBARAK HO. AAPNE YEH KHEL JEET LIYA HAI ")
    print("AAP LEKE JAA RAHE HAI Rs: "+str(score))                                         #begin by Function Calls
runGame()
