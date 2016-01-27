import random

import sys, time

def timed_raw_input(prompt, timeout):
    start = time.time()
    s = raw_input("(%ds) %s" % (timeout, prompt))
    stop = time.time()
    if stop-start > timeout:
        print "Sorry! You missed time limit!"
        return ''
    return s

def load_words():
  """Load words for game"""
  words = open('word.csv').read().splitlines()
  return words

def get_time(level):
  time = 5

  if level == 2:
  	time = 12
  elif level == 3:
  	time = 20
  elif level == 4:
    time = 25

  return time

def sort_words(words, score):

  level = 0

  if score < 500:
    level = 1
  elif score < 1000:
    level = 2
  elif score < 1500:
    level = 3
  else:
    level = 4

  return [word for word in words if int(word[1]) == level]

def ready():
   ans = raw_input("Are your ready? (Print 'yes' or 'no')\n")
   if ans == "yes":
     print "Now we go"
   elif ans == "no":
     print "wait"
     time.sleep(2)
     print "Hope you are ready now, otherwise come later."
   while not ans in ['yes', 'no']:
     print "Invalid input, try again."
     ans = raw_input("Are your ready? (Print 'yes' or 'no')\n")
     if ans == "yes":
       print "Now we go"
     elif ans == "no":
       print "wait"
       time.sleep(2)
       print "Hope you are ready now, otherwise come later"

import random

def typing():
  print "Welcome to the typing speed game!!!"
  print "You should type words as fast as you can if you want to win."
  ready()
  time.sleep(1)
  tries = 5
  score = 0

  words = load_words()

  word_levels = []

  while tries > 0:

    for word in words:
      word_levels.append(word.split(','))


    word_levels = sort_words(word_levels, score)

    word_level = random.choice(word_levels)

    word  = word_level[0]

    level = word_level[1]

    score_worth = int(level) * 100

    print "Level: " + level + "\n"
    print "Score: " + str(score) + "\n"
    print "Tries left: " + str(tries) + "\n"
    time.sleep(2)
    print "Word: " + word + "\n"
    

    user_input = timed_raw_input("Begin typing!!", int(get_time(int(level))))

    if user_input.lower().strip() == word.lower().strip():

      score += score_worth
    
      if score >= 4000:
        print "You win!Congratulations!!"

        tries = 0
      else:
        print ""
        print "You are right!" 
        print ""

    else:
      tries -= 1

      if tries == 0:
        print "You lost!"
      else:
        print ""
        print "You got it wrong!"
        print ""
typing()
      

	
	
	

     
   
