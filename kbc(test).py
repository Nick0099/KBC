import time

N = input("what is you name sir? ")
Name = N.capitalize()
hour = time.strftime('%H%M')
if hour >= '00:00' and hour < '12:00':
  print("Good Morning ", Name)
elif hour >= '12:00' and hour < '16:00':
  print("Good Afternoon ", Name)
elif hour >= '16:00' and hour < '20:00':
  print("Good Evening ", Name)
else:
  print("Good Night ", Name)
print(
    "There are 10 questions in this game each question has \n 4 options and you have to choose the correct option  \n from  the given options if the answer is right you win some money \n and if the answer is wrong you lose the game although  \n you can stop before a question you can also quit the game \n and take the money you have won till then "
)
print("Are you ready", Name, "?")
print(
    "1. For the first question \n'The International Literacy Day is observed on \n A.Sep 8 \n B.Nov 28 \n C.May 2'"
)
ans = input()
if ans.upper() == "A":
  print("Congratulations you have won 1000 rupees")
  cont = input(
      "Do you want to quit the game with 1k rupees or do you want to continue?(y/n)"
  )
  if cont.upper() == "Y":
    print("The next question is on your screen")
    print(
        "The language of Lakshadweep. a Union Territory of India, is \n A.Tamil \n B.Hindi \n C.Malayalam"
    )
    ans = input()
    if ans.upper() == "C":
      print("Congratulations you have won 2000 rupees")
      cont = input(
          "Do you want to quit the game with 2k rupees or do you want to continue?(y/n)"
      )
      if cont.upper() == "Y":
        print("The next question is on your screen")
        print(
            " In which group of places the Kumbha Mela is held every twelve years? \n A.Ujjain. Purl; Prayag. Haridwar \n B.Prayag. Haridwar, Ujjain,. Nasik \n C.Rameshwaram. Purl, Badrinath. Dwarika"
        )
        ans = input()
        if ans.upper() == "B":
          print("Congratulations you have won 3k rupees")
          cont = input(
            "Do you want to quit the game with 3k rupees or do you want to continue?(y/n)"
        )
          if cont.upper() == "Y":
            print("The next question is on your screen")
            print(
            "Bahubali festival is related to \n A.Islam \n B.Hinduism \n C.Buddhism"
        )
            ans = input()
            if ans.upper() == "B":
              print("Congratulations you have won 4k rupees")
            else:
              print("Sorry you have lost the game")
        else:
          print("Sorry you lost the game")
  else:
    print("Sorry you lost the game")
else:
  print("Sorry you lost the game")
print("Thank you for playing the game")