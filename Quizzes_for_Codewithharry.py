                            # Taskswithharry

# import time
# t = time.strftime('%H:%M:%S')  
#                 # only for hourssssssssssss
# # timestamp = int(time.strftime('%H')) 
# # print(timestamp) 

# # input_hours = int(input("Enter hours(1-24): "))
# input_hours = 11

# if (input_hours > 0 and input_hours < 12):
#     print("Good Morning bro!!!")
# elif (input_hours >= 12 and input_hours < 16):
#     print("Good Afternoon bro!!!")
# elif (input_hours >= 16 and input_hours < 20):
#     print("Good evening bro!!!")
# else:
#     print("Good day bro!!!")












# write a program that user and computer guessing a numbers: 
# import time
# t = time.strftime('%H:%M:%S')  
# print(t) 

# import random
# comp = random.randrange(1,10)
# user = int(input("Enter the no b/w (1 to 10): "))
# if user>comp:
#     print("User no ", user)
#     print("Computer no: ", comp)
#     print("Your guess no is too high")

# elif user < comp:
#     print("User no ", user)
#     print("Computer no: ", comp)
#     print("Your guess no is too Low")
    
# else:
#     print("User no ", user)
#     print("Computer no: ", comp)
#     print("Your guess no is equal")







# # create a function using a def keyword followed by a function name , followed by a parenthesis(()) and a colon (:)

# def greet(name):
#     print("Hello, " + name + ". How are you?")

# greet("Moiz")
# greet("Mansoori")





# create a function average of numbers from users

# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum +=i
#     avg = sum / len(numbers)
#     return avg
    
# # num1 = int(input("Enter 1st digit:"))
# # num2 = int(input("Enter 2nd digit:"))
# # num3 = int(input("Enter 3rd digit:"))
# num1 = 1
# num2 = 4
# num3 = 5
# result = average(num1 , num2 , num3 )
# print("Average is:", result)



# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     elif (n<0):
#         print("Negative number not allowed")
#     else:
#         return n * factorial(n-1)
    
# # txt = int(input("Enter number you want to factorial: "))
# txt = 10
# print(factorial(txt))





# QUIZ  write a program to print fibonacci series

# def fibonacci(num):
#     if(num == 1 or num <=0):
#         print("Please select number greater than 1")
#         return 0
#     else:
#         a , b = 0,1
#         print(a,b , end=" ")
#         for _ in range(num - 2):
#             next = a + b
#             print(next, end=" ")
#             a , b = b , next

# # terms = int(input("Enter the number of terms in Fibonacci series: "))
# terms = 15
# print(fibonacci(terms))












# create a program capable of displaying questions to the user like KBC. use list data types to store the question and their correct answers display the final amount person is taking home after playing the game




# import datetime

# x = datetime.datetime.now()
# print(x)

# questions = [
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0],
#     ["Which city is the capital of Pakistan in 1947?","A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad",0]

#     ]

# levels = [1000, 2000, 3000, 40000, 10000, 50000, 80000, 160000, 320000, 100000]
# money = 0

# for i in range(len(questions)):
#     question = questions[i]
#     print(f"Question for Rs. {levels[i]}")
#     print(question[0])  
#     print(f"1. {question[1]}")
#     print(f"2. {question[2]}")
#     print(f"3. {question[3]}")
#     print(f"4. {question[4]}")
#     reply = input("Enter your answer (1-4): ")

#     if reply == str(question[5] + 1): 
#         print(f"Correct Answer! You have won Rs. {levels[i]}")
#         if i == 3:
#             money += 10000
#         elif i == 8:
#             money += 100000
#         elif i == 9:
#             money += 1000000
#     else:
#         print("Wrong Answer")
#         break

# print(f"You take home money is Rs. {money}")



            # same same hai


# def KBCQuiz():
#     questions = [
#         "Which city is the capital of Pakistan in 1947?",
#         "Who is the innocent person in the world?",
#         "Which Country Moiz Mansoori love to go?",
#         "Which team won the T20 worldcup 2022?",
#     ]
#     options = [
#         ["A. Karachi", "B. Islamabad", "C. Lahore", "D. Hyderabad"],
#         ["A. Moiz", "B. Mansoori", "C. Moiz Mansoori", "D. Moiz Ahmed Mansoori"],
#         ["A. Spain", "B. France", "C. Germany", "D. England"],
#         ["A. Pakistan", "B. England", "C. Australia", "D. India"]
#     ]
#     correct_answers = ["A", "D", "A", "B"] 
    
#     prize_money = [1500, 3000, 3500, 2500]

#     total_prize = 0

#     print("\t\t\t\t\tWelcome to the Quiz Game!")
#     print("\t\t\tAnswer the following questions to win prize money.")

#     for i in range(len(questions)):
#         print("\nQuestion", i + 1, ":", questions[i])
#         for option in options[i]:
#             print(option)
#         user_answer = input("Enter your answer (A/B/C/D): ") 
    
#         if user_answer.upper() == correct_answers[i]:  
#             total_prize += prize_money[i]
#             print("Correct! You've won Rs", prize_money[i])
#         else:
#             print("Incorrect! Please try another answer to win prizes")

#     print("\nCongratulations! You're taking home Rs", total_prize)
# KBCQuiz()
















# write a python program to translate a message into secret code language. use he rule below the translate normal language into secret code language
# Coding
# if the word contain atleast three characters, remove the first letter and append it at the end
# now append three random character at the starting and the end
# else:
#     simply reverse the string
# Decoding:
#     if the word contain at least three character reverse it 
# else:
#     remove three character at the start and end. Now remove the last letter and appending at the beigning


# st = "Moiz is good"
# words = st.split(" ")
# coding = True
# if(coding):
#     nwords = []
#     for word in words:
#         if(len(word)>=3):
#             r1 = "asy"
#             r2 = "dfs"
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))

# else:
#     nwords = []
#     for word in words:
#         if(len(word)>=3):
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))
    


                # Cheating krky kra h 
# import random

# def encode(message):
#     if len(message) >= 3:
#         first_letter = message[0]
#         message = message[1:] + first_letter
#         random_chars = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
#         encoded_message = random_chars + message + random_chars
#     else:
#         encoded_message = message[::-1]
    
#     return encoded_message

# def decode(encoded_message):
#     if len(encoded_message) >= 3:
#         decoded_message = encoded_message[::-1]
#     else:
#         random_chars = encoded_message[:3]
#         message = encoded_message[3:-1]
#         last_letter = encoded_message[-1]
#         decoded_message = last_letter + message
    
#     return decoded_message

# # Test the encoding and decoding
# message = "Moiz is good "
# encoded = encode(message)
# print("Encoded:", encoded)

# decoded = decode(encoded)
# print("Decoded:", decoded)




# write a program gun , water and snake (computer vs user )   

# import random
# def check(comp , user):
#     if comp == user:
#         print("It's a tie, try again")
#         return 0
#     elif (comp == 0 and user ==1) or (comp == 1 and user == 2) or (comp ==2 and user == 0):
#         print("You lose, computer wins!!")
#         return 0
#     else:
#         print("You WINNNNNN!!! Computer loses")
#         return 1
        
# comp = random.randint(0,2)
# user = int(input("Enter any number: 0 for Snake , 1 for Water and 2 for Gun: "))
# print("You: ", user)
# print("Computer: ", comp)
# score = check(comp , user)





# write a library class with no_of_books as two instance. write a program to create a library from this library class and show how you can print all books, add a book and get the number of books using different methods. show that your program doesnot presist the bookafter the program is stopped! 

# class Library:
#     def __init__(self, no_books):
#         self.no_books = no_books
#         self.books = []

#     def add_books(self, book_name):
#         self.books.append(book_name)
#         self.no_books = len(self.books)
#         print(f"Book '{book_name}' added in the library")

#     def get_books(self):
# #         return self.books

#     def get_no_books(self):
#         return self.no_books

# def main():
#     no_books = 0
#     library = Library(no_books)

#     while True:
#         print("\n1. Print all books")
#         print("2. Add a book")
#         print("3. Get number of books")
#         print("4. Exit")
#         choice = input("Enter the number:")

#         if choice == "1":
#             books = library.get_books()
#             if books:
#                 for book in books:
#                     print(book)
#             else:
#                 print("Library is empty")

#         elif choice == "2":
#             book_name = input("Enter the book name: ")
#             library.add_books(book_name)

#         elif choice == "3":
#             num_books = library.get_no_books()
#             print(f"Number of books in the library: {num_books}")

#         elif choice == "4":
#             print("Exit the program (Library)")
#             break

#         else:
#             print("Invalid choice. Please choose a valid option.")

# if __name__ == "__main__":
#     main()





