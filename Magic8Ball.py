#Magic8Ball.py
#Name:Gavin Grow
#Date:2/1/26
#Assignment:Magic 8 Ball

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  answers = ["It is decidedly so", "It is certain","Without a doubt", "Yes definitely","You may rely on it","As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again later","Ask again later","Better not tell you now", "Cannot predict now", "Concentrate and ask again". "Dont count on it", "My reply is no","My sources say no","Outlook not so good", "Very doubtful"]
  length = len(answers)           
  print("Magic 8 Ball")
  #Prompt the user for their question.
input ("What is your question?:")
  #Answer question randomly with one of the options from your earlier list.
answers 
r = random.random() *length
if __name__ == '__main__':
  main()
