import random

class Welome:
  def __init__(self):
    print("Welcome to Smart Learning Hub!")

class QuestionGame:
  # random_question_and_answer_dictionary method return a dictionary of question with question as key and answer as value
  def random_question_and_answer_dictionary(self):
    question = {"What is quantum entanglement?": "A phenomenon where particles remain connected across space", "What is the event horizon of a black hole?": "The boundary beyond which nothing, not even light, can escape", "What does the Heisenberg Uncertainty Principle state?": "The more precisely we know a particle’s position, the less precisely we can know its momentum", "What is Hawking radiation?": "Radiation that black holes emit due to quantum effects near the event horizon", "What is a wormhole theorized to be?": "A shortcut through spacetime connecting distant regions of the universe"}
    return question
  
  # check_answer takes in 2 values the correct option and the correct answer and it checks if the correct option is 
  # equal to correct answer and it returns correct and if its no the same it returns try again 2 more time in total 3 tries
  def check_answer(self,correct_option, correct_answer):
    correct_option = int(correct_option)
    while True:
      try:
        answer = int(input("Select the correct option number: "))
      except ValueError:
        print("Invalid Input: Please enter a number")
        continue
      if type(answer) != int or answer > 4 or answer <=0:
        print("Invalid Input: Please enter a number")
      else:
        break
        
    for i in range(1,4): 
      if answer == correct_option:
        print("Congratulation Correct answer\n ----------------------------" )
        break    
      elif i == 3:
        print("No more tries left\nCorrect answer is option",correct_option, ": ", correct_answer ," \n ----------------------------")
      else:
        try:
          answer = int(input("Try again: "))
        except ValueError:
          print("Invalid Input: Please enter a number")



  # asking_question_with_answer randomly selectes a question and correct answer from the question dictionary returned by random_question_and_answer_dictionary
  #and insert the correct answer within a list of 3 more predefined wrong answers ans return a dictionary with option number and answers
  def asking_question_with_answer(self):

    questions = self.random_question_and_answer_dictionary()

  
    ask_question = random.choice(list(questions.keys()))
    correct_answer = questions[ask_question]
    option_num = ["1", "2", "3", "4"]
    option_ans = ["A particle orbiting at relativistic speed",
                  "An electromagnetic pulse from a neutron star",
                  "A distortion caused by space dust interaction"]
    option_ans.append(correct_answer)
    random.shuffle(option_ans)


    final_question_dict = dict(zip(option_num, option_ans))
    for key, value in final_question_dict.items():
      if value == correct_answer:
        break
    correct_option = (key)
    print(f"Question : {ask_question}")
    for idx, opt in enumerate(option_ans, start=1):
      print(f"Option {idx}: {opt}")

    self.check_answer(correct_option, correct_answer)
  



# Score calculator intakes a value and returns the grade
class ScoreCalculator:

  def score_cal(self,score):

    print("----------------------------")
    grade = ''
    if score >= 90:
      grade = 'Excellent'
    elif (score >= 75) and (score <= 89):
      grade = 'Good'
    elif (score >= 50) and (score <= 74):
      grade = 'Satisfactory'
    elif score < 50:
      grade = 'Needs Improvement'
    return grade


  def get_score_for_5_subjects(self):

    subjects = ['subject_1', 'subject_2','subject_3', 'subject_4','subject_5']
    Total_score = 0
    subjects_score = {}
    for subject in subjects:
      while True:
        try:
          subject_score = int(input(f"Enter {subject} score: "))
        except ValueError:
          print("Invalid Input: Please enter a number")
          continue
        if subject_score > 100 or subject_score < 0:
          print("Invalid Input Enter a value between 0 - 100")
          continue
        else:
          break
      
      Total_score += subject_score
      subject_grade = self.score_cal(subject_score)
      subjects_score[subject] = subject_grade
    
    avg_score = Total_score/5

    for k, v in subjects_score.items():
      print(f"{k} : {v}")
    
    print("Average Score: ",avg_score)


class Game(Welome):
  def __init__(self):
    print("----------------------------") 
    super().__init__()
    print("----------------------------") 
    exitnow = True
    while exitnow:
      begin = int(input("Select a option below\n\n 1: Start the Smart Quiz Game\n 2: Use the Student Performance Tracker\n 3: Exit the program\n Enter: "))

      if begin == 1:
        print("----------------------------")  
        print("Let begin the quiz")
        print("----------------------------")
        game = QuestionGame()
        game.asking_question_with_answer()
      elif begin == 2:
        score = ScoreCalculator()
        score.get_score_for_5_subjects()
        print("----------------------------")
      elif begin == 3:
        exitnow = False
      else:
        print("Invalid Input please enter from options provided")


start_game = Game()
start_game


