questions =[
["The International Literacy Day is observed on", " A.Sep 8", "B.Nov 28", "C.May 2", "D.Sep 22", 1],
  ["The language of Lakshadweep. a Union Territory of India,is", "A.Tamil", "B.Hindi", "C.Malayalam", "D.Telugu", 3],
  ["In which group of places the Kumbha Mela is held every twelve years?", "A.Ujjain. Purl; Prayag. Haridwar", "B.Prayag. Haridwar, Ujjain,. Nasik", "C.Rameshwaram. Purl, Badrinath. Dwarika","D.Chittakoot, Ujjain, Prayag,'Haridwar", 2],
["Bahubali festival is related to", "A.Islam", "B.Hinduism", "C.Christianity", "D.Jainism", 4],
["Which day is observed as the World Standards Day?", "A.June 26","B.Oct 14", "C.Nov 15", "D.Dec 2", 2],
["Which of the following was the theme of the World Red Cross and Red Crescent Day?", "A.Dignity for all - focus on women","B.Dignity for all - focus on Children", "C.Focus on health for all","D.Nourishment for all-focus on children", 2],
  ["September 27 is celebrated every year as", "A.Teachers' Day","B.National Integration Day", "C.World Tourism Day","D.International Literacy Day", 3],
["Who is the author of 'Manas Ka-Hans' ?", "A.Khushwant Singh", "B.Prem Chand", "C.Jayashankar Prasad", "D.Amrit Lal Nagar", 2],
["The death anniversary of which of the following leaders is observed as Martyrs' Day?", "A.Smt. Indira Gandhi", "B.PI. Jawaharlal Nehru", "C.Mahatma Gandhi", "D.Lal Bahadur Shastri", 4],
["Who is the author of the epic 'Meghdoot'?", "A.Vishakadatta", "B.Valmiki","C.Banabhatta", "D.Kalidas", 4],
["Which of the following is observed as Sports Day every year?","A.22nd April", "B.26th  july", "C.29th August", "D.2nd October", 2],
["Pongal is a popular festival of which state?", "A.Karnataka", "B.Kerala", "C.Tamil Nadu", "D.Andhra Pradesh", 1],
["Ghototkach in Mahabharat was the son of", "A.Duryodhana", "B.Arjuna", "C.Yudhishthir", "D.Bhima", 3],
["Which of the following is a popular sport in Kerala?", "A.Volleyball", "B.Cricket", "C.Badminton", "D.Hockey", 4],
["Which of the following is spoken by the people of the Andaman and Nicobar Islands?","A.Dutch", "B.Malyalam", "C.Telegu", "D.Malayalam", 4],
["The International Literacy Day is observed to commemorate the book", "A.Indian Education", "A.Indian Economy", "C.Indian History","D.Indian Literature", 3],
["The language of Lakshadweep. a Union Territory of India,is", "A.Tamil","B.Hindi", "C.Malayalam", "D.Telugu", 3 ],
]
levels = [ 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 250000, 2500000, 5000000, 10000000, 70000000, 100000000]
money = 0
for i in range(0, len(questions)):
  question = questions[i]
  print(f"Question for Rs. {levels[i]}")
  print(question[0])
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:" ))
  if (reply == 0):
    money = levels[i-1]
    break
  elif(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Thank you for playing KBC.Yo'ur going home with Rs. {money}")
