"""
Names: Sophie Goldensohn and Sabina Cherner
Name of Project: Mad Libs
"""

word1 = input("Enter a first name: ")
word2 = int(input("Enter a number: "))
word3 = input("Enter a city/town: ")
word4 = input("Enter a US President's last name: ")
word5 = input("Enter a last name: ")
word6 = input("Enter an adjective: ")
word7 = input("Enter a verb ending in -ing: ")
word8 = input("Enter an adjective: ")
word9 = input("Enter a percentage: ")
word10 = input("Enter a class: ")
word11 = input("Enter a profession: ")
word12 = input("Enter a direction: ")
word13 = input("Enter another adjective: ")

if word2 <= 18 :
  print("My name is", word1, "and I am", word2, "years old. I just moved to", word3, "and attend", word4, "High School. Yesterday, my teacher Ms.",word5, word6, "accused me of", word7, "the principal's", word8, "face.")

elif 24 >= word2 >= 19 :
  print("College is so", word6,"! This fall, I left home and went to", word4, "College in", word3,". I'm taking", word10, "to become a", word11,". I was always the", word8, "student in high school. Now, my test average is", word9,"%! My", word13, "friends can't believe it. Hopefully this year, I can get my grades", word12, "by", word7, "with my teacher.")