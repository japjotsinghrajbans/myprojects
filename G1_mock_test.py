"""
author: Japjot Singh Rajbans
created on: 16 November 2024
completed on: 17 November 2024
title: G1 Mock Test
"""

# Introduction
print("--------------------------------------------")
print("Welcome to the G1 Ontario Mock Test made by Japjot!")
print("Each question is worth 1 mark.")
print("These are MCQs covering various topics like road signs, traffic laws, and safe driving practices.")
print("Remember: stay calm, answer wisely, and all the best! :)")
print("--------------------------------------------")
input("Press 'Enter' to begin this mock test...")
print("--------------------------------------------")

# The Score
points = []

# The Test
# Question 1
question_1 = input("Q1) If a fully licensed driver is convicted of using a hand-held electronic device while driving, they will face which of the following penalties for a first offence?\na) A fine of up to $1,000 and 3 demerit points\nb) A fine of up to $500 and 2 demerit points\nc) A 30-day licence suspension\nd) None of the above\nAnswer: ")
if question_1.lower() == "a)" or question_1.lower() == "a":
    print(">>> That's correct! :)")
    point_1 = 1
    points.append(point_1)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: a)")
    point_1 = 0
    points.append(point_1)

# Question 2
question_2 = input("Q2) You will receive _____ the first time you are convicted of a Criminal Code offence.\na) a one-year licence suspension\nb) a lifetime ban from driving\nc) a one-month licence suspension\nd) a two-year licence suspension\nAnswer: ")
if question_2.lower() == "a)" or question_2.lower() == "a":
    print(">>> That's correct! :)")
    point_2 = 1
    points.append(point_2)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: a)")
    point_2 = 0
    points.append(point_2)

# Question 3
question_3 = input("Q3) Under Ontario's Move Over law, you are required to...\na) pull over if an emergency vehicle is following you with its lights flashing.\nb) change lanes if safe when passing a stopped emergency vehicle with its lights flashing\nc) move into the rightmost lane if you are driving slower than other traffic.\nd) do none of the above.\nAnswer: ")
if question_3.lower() == "b)" or question_3.lower() == "b":
    print(">>> That's correct! :)")
    point_3 = 1
    points.append(point_3)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: b)")
    point_3 = 0
    points.append(point_3)

# Question 4
question_4 = input("Q4) Do NOT park anywhere that you don't have a clear view for at least ___ metres in both directions.\na) 125\nb) 135\nc) 150\nd) 175\nAnswer: ")
if question_4.lower() == "a)" or question_4.lower() == "a" or question_4 == "125":
    print(">>> That's correct! :)")
    point_4 = 1
    points.append(point_4)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: a) or 125 metres, in this case")
    point_4 = 0
    points.append(point_4)

# Question 5
question_5 = input("Q5) You may NOT park within _ ______ of an intersection that is NOT controlled by traffic lights.\na) 5 metres\nb) 7 metres\nc) 9 metres\nd) 15 metres\nAnswer: ")
if question_5.lower() == "c)" or question_5.lower() == "c" or question_5 == "9 metres":
    print(">>> That's correct! :)")
    point_5 = 1
    points.append(point_5)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: c) or 9 metres, in this case")
    point_5 = 0
    points.append(point_5)

# Question 6
question_6 = input("Q6) While driving, a Class G1 learner must be supervised by an accompanying driver. The blood-alcohol level of the accompanying driver must be less than...\na) 0.02%\nb) 0.05%\nc) 0.07%\nd) 0.08%\nAnswer: ")
if question_6.lower() == "b)" or question_6.lower() == "b" or question_6 == "0.05" or question_6 == "0.05%":
    print(">>> That's correct! :)")
    point_6 = 1
    points.append(point_6)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: b) or 0.05%, in this case")
    point_6 = 0
    points.append(point_6)

# Question 7
question_7 = input("Q7) If you are found guilty of backing on a highway or driving too slowly, _ demerit points will be added to your driving record.\na) 5\nb) 3\nc) 2\nd) 1\nAnswer: ")
if question_7.lower() == "c)" or question_7.lower() == "c" or question_7 == "2":
    print(">>> That's correct! :)")
    point_7 = 1
    points.append(point_7)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: c) or 2, in this case")
    point_7 = 0
    points.append(point_7)

# Question 8
question_8 = input("Q8) A G2 driver age 19 or younger who has 6 months or less of driving experience may carry _ unrelated passenger(s) age 19 or younger between midnight and 5 AM.\na) 1\nb) 2\nc) 3\nd) 4\nAnswer: ")
if question_8.lower() == "a)" or question_8.lower() == "a" or question_8 == "1":
    print(">>> That's correct! :)")
    point_8 = 1
    points.append(point_8)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: a) or 1, in this case")
    point_8 = 0
    points.append(point_8)

# Question 9
question_9 = input("Q9) If you are convicted of following too closely (tailgating), _ demerit points will be added to your driving record.\na) 4\nb) 5\nc) 2\nd) 6\nAnswer: ")
if question_9.lower() == "a)" or question_9.lower() == "a" or question_9 == "4":
    print(">>> That's correct! :)")
    point_9 = 1
    points.append(point_9)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: a) or 4, in this case")
    point_9 = 0
    points.append(point_9)

# Question 10
question_10 = input("Q10) What does the sign with an orange background and an arrow pointing at top left mean?\na) Closed lane\nb) Road turns left\nc) Slight bend or curve in the road ahead\nd) Yield to the left\nAnswer: ")
if question_10.lower() == "a)" or question_10.lower() == "a" or question_10 == "Closed lane":
    print(">>> That's correct! :)")
    point_10 = 1
    points.append(point_10)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: a) or Closed lane, in this case")
    point_10 = 0
    points.append(point_10)

# Question 11
question_11 = input("Q11) A G2 driver age 19 or younger who has more than 6 months of driving experience may carry _ unrelated passenger(s) age 19 or younger between midnight and 5 AM.\na) 1\nb) 2\nc) 3\nd) 4\nAnswer: ")
if question_11.lower() == "c)" or question_11.lower() == "c" or question_11 == "3":
    print(">>> That's correct! :)")
    point_11 = 1
    points.append(point_11)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: c) or 3, in this case")
    point_11 = 0
    points.append(point_11)

# Question 12
question_12 = input("Q12) If you are convicted for the first time of driving while your licence is suspended, you will get an additional six-month suspension, and you will also face which of the following additional penalties?\na) A fine of between $1,000 and $5,000\nb) Either jail time or a fine or both\nc) Six months in jail\nd) Neither jail time nor a fine\nAnswer: ")
if question_12.lower() == "b)" or question_12.lower() == "b":
    print(">>> That's correct! :)")
    point_12 = 1
    points.append(point_12)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: b)")
    point_12 = 0
    points.append(point_12)

# Question 13
question_13 = input("Q13) What does the sign with a thick road strip on the left and 'Do not cross' written on the right mean?\na) Vehicles cannot change lanes into or out of a high-occupancy vehicle (HOV) lane in this area.\nb) There is a railway crossing ahead. Be alert for trains.\nc) There is a hazard close to the edge of the road. The downward lines show the side on which you may safely pass.\nd) There is a pedestrian crossover. Be prepared to stop and yield the right-of-way to pedestrians.\nAnswer: ")
if question_13.lower() == "a)" or question_13.lower() == "a":
    print(">>> That's correct! :)")
    point_13 = 1
    points.append(point_13)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: a)")
    point_13 = 0
    points.append(point_13)

# Question 14
question_14 = input("Q14) If you are found guilty of going the wrong way on a one-way road, _ demerit points will be added to your driving record.\na) 2\nb) 5\nc) 6\nd) 3\nAnswer: ")
if question_14.lower() == "d)" or question_14.lower() == "d" or question_14 == "3":
    print(">>> That's correct! :)")
    point_14 = 1
    points.append(point_14)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: d) or 3 demerit points, in this case")
    point_14 = 0
    points.append(point_14)

# Question 15
question_15 = input("Q15) If you are found guilty of carrying a child passenger who is not properly secured, _ demerit points will be added to your driving record.\na) 2\nb) zero\nc) 4\nd) 3\nAnswer: ")
if question_15.lower() == "a)" or question_15.lower() == "a" or question_15 == "2":
    print(">>> That's correct! :)")
    point_15 = 1
    points.append(point_15)
else:
    print(">>> Sorry, that's not correct! :(")
    print(">>> The correct answer is: a) or 2 demerit points, in this case")
    point_15 = 0
    points.append(point_15)

# Final Result
obtained_marks = sum(points)
total_marks = 15
percentage = (obtained_marks / total_marks) * 100
print("--------------------------------------------")
print(f">>> Your total score is: {obtained_marks}/{total_marks}")
print(f">>> Your percentage is: {percentage}")
if percentage > 79.9:
    print(">>> Congratulations! You have passed the G1 Mock Test! I know you will do well in the real test! :D")
else:
    print(">>> Oh well, better luck next time! :/")