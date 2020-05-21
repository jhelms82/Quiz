# INF360 - Programming in Python
# James Helms
# Mid term Project
# NFL 5 Question Quiz
# (20 points) Does the program execute with no errors
# (20 points) The program should contain: Good flow control, good use of functions, code should be as clean as possible (i.e. writing the smallest amount of code necessary to complete the function), and contain examples of lists or dictionaries
# (20 points) The project should be well documented. Make use of block and line comments to describe the program as a whole, individual functions, and major areas of the project.
# (20 points) Use of the logging module. This should be used in place of where you might have had print statements (unless your project was intended to have console output. Refer to Chapter 10 – Debugging. You should import the module, setup the basic config, and then you must have a combination of logging.debug and logging.critical statements used appropriately. You can use any additional logging level you choose, possibly logging.warning
# (20 points) Use of Object-Oriented Programming. This can be you creating your own classes and modules OR the use of third party modules. If using third party modules, be sure to put in the comments the packages that need to be installed (probably from pip).

#import logging for the logging.basicconfig
import logging
import sys



#Logging config which is in function.py file
logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')


#Have try and except name introduction function in missing function.py file and using logging criteria. 
try:
    import function as fn
except:
    logging.critical('Missing fucntion.py!')
    print('Missing functionn.py! Program is closing')
    sys.exit()



#Creating questions class using def init method with self.prompt and self.answer    
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
#Question prompts  which includes the list of questions including with multiple choice options       
question_prompts = [
        "What team won Super Bowl 54?\n(a) 'Kansas City Chiefs'\n(b) 'New England Patriots'\n(c) 'Baltimore Ravens'\n(d) 'San Francisco 49ers'\n\n Please enter a, b, c, or d. Then hit enter:",'\n'
        "What player won Super 54 MVP?\n(a) 'Tom Brady'\n(b) 'Lamar Jackson'\n(c) 'Patrick Mahomes'\n(d) 'Damien Williams'\n\n Please enter a, b, c, or d. Then hit enter:",'\n'
        "Who won the NFL regular season MVP?\n(a) 'Patrick Mahomes'\n(b) 'Nick Bosa'\n(c) 'Michael Thomas'\n(d) 'Lamar Jackson'\n\n Please enter a, b, c, or d. Then hit enter:",'\n'
        "What team will Tom Brady play for in 2020?\n(a) 'Denver Broncos'\n(b) 'Tampa Bay Bucaneers'\n(c) 'New England Patriots'\n(d) 'Houston Texans'\n\n Please enter a, b, c, or d. Then hit enter:",'\n'
        "Who led the NFL in receiving yards in the 2019 season?\n(a) 'Michael Thomas'\n(b) 'Tyreek Hill'\n(c) 'Odell Beckham Jr.'\n(d) 'Antonio Brown'\n\n Please enter a, b, c, or d. Then hit enter:",'\n'
    ]

#questions array for question answers from the question prompts which include the answers from each question

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "c"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a")
              ]

# Current points they start out with, which would obviously be 0
score = 0            




#function to run quiz so it can loop through all the questions score starts out 0, user will allow answer input, if correct, they get 1 point, if wrong 0. Also has if and else statement with the answer answer.
def run_quiz(questions):
    score = 0
for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
          if answer == question.answer:
              print()
              print("You are correct!!!")
          else:
            print()
            print("You are wrong! The correct answer is", question.answer)
            print()





#Have if and else expression for results for how well they did at the end of the quiz
if score <= 2:
    print(fn.name, "thank you for taking the NFL quiz you got", score, "out of", len(questions),"You need to pay more attention!")
elif score == 3:
    print(fn.name, "thank you for taking the NFL quiz you got", score, "out of", len(questions),"You did very average.")
elif score == 4:
    print(fn.name, "thank you for taking the NFL quiz you got", score, "out of", len(questions),"You did a great job!")
else:
    print (fn.name, "thank you for taking the NFL quiz you got", score, "out of", len(questions),"Wow perfect score! You are a NFL Wizard!!!")




