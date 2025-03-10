# quiz game in python
# static quiz game
print("***QUIZ-TEST***")
print("Sign in:")
user_password = {"sachin_rajpoot": 8081,
                "sanjana_rajpoot": 9399,
                "manish_rai":8080,
                "deepak" :  9005,
                "raj_kumar" : 4000,
                "rahul_kumar":5050,
                 "john_das":5057,
                 "lasith_malinga":1111,
                 "jos_butler":2089
                 }

username=user_password.keys()
userpass=user_password.values()

#user  name varification function :

def  authentication():
 user=input("Enter your user_id :")
 if user in username:
  print(f"hello { user} ")
 else:
  print("enter a valid user !")
  authentication()
authentication()

# user passsword varification function:

def authentication2():
    passt=int(input("enter your password :"))
    if passt in userpass:
        print("")
    else:
        print("enter a valid password!")
        authentication2()
authentication2()
user=input("enter your full name for result: ")

print("now you are in test... ")

# question sets
questions = ("how many state in india ?",
             "what is the capital of madhyapradesh ?",
             "how many planet in space ? ",
             "who is the prime minister of america ?",
             "what is the position of j in alphabets ?",
             "who is the father of C language ?",
             "which language are known as silk ?",
             "how many layer in OSI model ?",
             "what is the name of % sign in technical way ?",
             "what is the smallest unit of program ?",
             "how many week in a year ?",
             "what is the unit of power ?",
             "who is prime minister of india ?",
             "how many vowel in alphabets ?",
             "what is the superlative of GOOD ?",
             "what is the opposite of BOttOM ?",
             "where is Tajmahal ?",
             "what is the full form of BCA ?",
             "who is father of india ?",
             "what is the full form of RAM ?",

             )

options=(("A. 23","B. 28","C. 29","D. 26"),
         ("A. DELHI","B. VIDISHA","C. BHOPAL","D. INDORE"),
         ("A. 8","B. 9","C. 10","D. 7"),
         ("A. TRUMP","B. MODI","C. ADAM","D. MARKRAM"),
         ("A. 20","B. 14","C. 10","D. 11"),
         ("A. guido van","B. dannis richie","C. paul","D. john"),
         ("A. java","B. C++","C. python","D. SQL"),
         ("A. 2","B. 4","C. 6","D. 7"),
         ("A. modulas","B. percentage","C. devider","D. none of these"),
         ("A. function","B. class","C. Token","D. library"),
         ("A. 50","B. 52","C. 55","D. 53"),
         ("A. watt","B. ohm","C. meter","D. inch"),
         ("A. narendra modi ","B. rahul gandhi","C. seeta raman","D. jay shah"),
         ("A. 2","B. 4","C. 5","D. 6"),
         ("A. better","B. bad","C. good","D. best"),
         ("A. top","B. down ","C. up","D. none of these"),
         ("A. agra","B. delhi","C. mathura","D. kanpur"),
         ("A. none of these","B. bachelor of count applicaton","C. bachelor of computer application","D. bachelor of computer app "),
         ("A. bhagat singh","B. modi ji ","C. gandhi ji  ","D. nehru ji "),
         ("A. random access memory ","B. redonel access memory ","C. round access memory ","D. none of these"))

answers=("B","C","A","A","C","B","A","D","A","C","B","A","A","C","D","C","A","C","C","A")
gusses=[]
score=0
question_num=0

for question in questions:
    print("____________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Choose answer | A | B | C| D|....").upper()
    gusses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        score-=1 #minus marking
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1
print("______________________")
print("      RESULT :         ")
print("______________________")

print(" answer:", end="")
for answer in answers:
    print(answer ,end=" ")
print()
print("guesses:",end="")
for guess in gusses:
    print(guess,end=" ")
print()
score=(score/len(questions)*100)
print("________________")
print(f"your score is {score}%")
if score>=60:
    print("________________")
    print(f"{user} you are qualify the TEST ")
    print("________________")
    print("Status: PASSED")
    print("________________")
else:
    print(f"{user} you failed! in TEST")
    print("________________")
    print("Status: FAIL")
    print("________________")


