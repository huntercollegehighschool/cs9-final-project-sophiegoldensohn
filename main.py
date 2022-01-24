"""
Names: Sophie Goldensohn and Sabina Cherner
Name of Project: Mad Libs
*We decided to have the user's input for the third prompt determine the story they will recieve. If we were to randomly select one of the four stories- we'd do this with the random.choice() function that would choose an integer 1-4, each of which would each be assigned to one of the four storylines*
"""
print ("Hi! Please answer the following prompts. We will then give you a story that aligns with you age!")
name = input("Enter a first name: ")
name2 = input ("Enter another name: ")
age = int(input("Enter an age: "))
citytown = input("Enter a city/town: ")
schoolname = input("Enter a US President's last name: ")
lastname = input("Enter a last name: ")
adj = input("Enter an adjective: ")
adj2 = input ("Enter an adjective that ends in -iest: ")
food = input("Enter a food: ")
percent = input("Enter a percentage: ")
subject = input("Enter an academic subject: ")
profession = input("Enter a profession: ")
profession2 = input ("Enter another profession: ")
activity = input ("Enter your favorite activity that ends in -ing: ")
negemotion = input ("Enter a negative emotion: ")
posemotion = input ("Enter a positive emotion: ")
movie = input ("Enter a movie: ")
activity2 = input ("Enter an activity that DOESN'T end in -ing: ")
endtime = input ("Enter a time: ")
number = input ("Enter a number: ")

if 0 <= age <= 12  :
  print("Hello. I am" + name + ". I am ", age, ". My birthday is in " + number+ " days and then I will turn", age+1, "! When I grow up I want to be a "+ profession+ " and my best friend "+ name2+ " is going to be a "+ profession2 + "! My teacher is named Ms. " + lastname + " and I love her. In fact, she is the " + adj2 + " person I've ever met! She even taught me how to make " + food + " which is my favorite snack! I'm always " + posemotion + " at school and I can't wait to go back tomorrow at "+ endtime+ ".")

elif 13 <= age <= 18 :
  print("Hi! My name is "+ name + " and I am ", age, " years old. I just moved to "+ citytown + " and go to "+ schoolname + " School. Yesterday, my teacher Ms. " + lastname + " wouldn't let me go " + activity + "! That made me really " + negemotion + ". For lunch I had some homemade " + food + " and then I played with my friend " + name2 + ". After that, I had to " + activity2 + " until school ended and I finally got to go home at " + endtime+ ".")

elif 19 <= age <= 24 :
  print("College is so " + adj + "! This fall, I left home and went to " + schoolname + " College in " + citytown + ". I'm taking " + subject + " to become a " + profession + ". I was always the " + adj2 + " student in high school. Now, my test average is " + percent + "%! My friends can't believe it. I think my professor has it out for me! Maybe this year, I can fix my grades by buying them some " + food + " and go watch " + movie + ". It'll end pretty late- at " + endtime + " so I hope I can stay awake. Overall, I'm just really " + posemotion + "!")

elif 25 <= age:
  print ("Hey! I'm " + name + " and I just turned ", age, number + " days ago! I recently graduated college with a masters in " + subject + " and I'm actually moving to " + citytown + " to pursue my career as a " + profession +". I'm also excited to make new friends! So far, I only know one person " + name2 + " who lives there. I'm a " + profession + " and " + name2 + " is a " + profession2 + "! They're going to take me " + activity + " tomorrow. I'm so excited because it will be my first time. Then, after we're going to grab some " + food + ".")

  