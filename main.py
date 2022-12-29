import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#rps_game=list(rock,paper,scissors)
answer=int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))
comp_choice=random.randint(0,2)
imgs=[rock,paper,scissors]

if(answer<0 or answer>2):
 print("invalid number!")
else:
   print("you chose:")
   imgs[answer]
   print("computer chose:")
   imgs[comp_choice]
  
   if(comp_choice==2 and answer==0):
    print("you won!")
   elif(answer==2 and comp_choice==0):
     print("you lost!")
   elif(comp_choice > answer):
     print("you lost!")
   elif(comp_choice == answer):
     print("its a tie!")
   else:
     print("invalid number")