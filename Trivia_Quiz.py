# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
def play_game():
    question_number = 0
    score = 0
    
    questions_list = ["Which country gave the Statue of Liberty to US?","What is the real name of The Flash?","Where is the world's quietest room located?","What is Tony Stark's phone number on Thor's Hammer?","The place with the longest name in the world has how many characters?","What is the most popular name in the world?","What is the densest planet in the Solar System?"]
    choices_list = [['1. Spain','2. France','3. Japan'],['1. Larry Allen','2. Harry Allen','3. Barry Allen'],['1. Singapore','2. India','3. USA'],['1. 212-970-4133','2. 212-971-4133','3. 212-972-4133'],['1. 85','2. 90','3. 98'],['1. John','2. Muhammad','3. Seo-Yeon'],['1. Earth','2. Jupiter','3. Mercury']]
    correct_list = ['2','3','3','1','1','2','1']
    
    while question_number != 5:
        question = random.choice(list(questions_list))
        question_index = questions_list.index(question)
        correct = correct_list[question_index]
        print(question)
        
        for choices in choices_list[question_index]:
            print(choices)
        answer = input("Answer: ")
        if answer == correct:
            score += 2
            print("Correct!\n")
        else:
            print("Wrong\n")
            
        questions_list.pop(question_index)
        choices_list.pop(question_index)
        correct_list.pop(question_index)
        question_number += 1
        
    if score >= 7:
        print("\nCongratulations! Your score is " + str(score))
    else:
        print("\nYour score is " + str(score) + ". Better luck next time!")
        
        
 #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        
name = input("Hi! What's your name? ")
print("\nHi, " + name + "! TRIVIA TIME!")

choice = ''
while choice != '0':
    print("\n--------------------------------")
    print("[1] Start!")
    print("[0] Quit")
    print("--------------------------------")
    
    choice  = input("\nStart or Quit? (1 or 0) ")
    if choice == '1':
        print("\nAlright! Here we go.\n")
        play_game()
    elif choice == '0':
        print("\nSee you later! ")
    else:
        print("\nSorry I don't understand. Please choose between 1 and 0.")
















        
        
        
        
        