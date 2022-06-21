# # functions

# def newFunc(*names):
#     for name in names:
#         print(f"{name} welecome to python")

# newFunc("joe", "jane", "jim")

num = "yes"
score = 0
while (num == "yes" or num == "y"):
 
    # Question 1

    answer1=input ("\nQ1. how many alphabets are their in an english language? \n (a) 28 \n (b) 21 \n (c) 24 \n (d) 23 \n Answer :")

    if answer1 == "c" or answer1 == "24":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")
        
    else:
        print("incroct the answer is (c) 24.")
        print("score", score )
        print("\n")
        
        
        # Question 2

    answer2=input ("Q2. what is the full form of pmmc ? \n (a) permanent magnet moving coil  \n (b) pretend magnet moving coil  \n (c) potencial magnet moving coil  \n (d) packed magnet moving coil  \n Answer :")

    if answer2 == "a" or answer2 == "permanent magnet moving coil ":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")
        
    else:
        print("incroct the answer is (a) permanent magnet moving coil .")
        print("score", score )
        print("\n")
        
        
        # Question 3
        
    answer3=input ("Q3. how many vovels are their in an english language? \n (a) 8 \n (b) 6 \n (c) 5 \n (d) 10 \n Answer :")

    if answer3 == "c" or answer3 == "5":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")

    else:
        print("incroct the answer is (c) 5.")
        print("score", score )
        print("\n")
        
        
    # Question 4

    answer4=input ("Q4. who is Abdul Kalam of indian government ? \n (a) 11th president \n (b) The Messile Man \n (c) Scientist \n (d) Teacher \n Answer :")

    if answer4 == "a" or answer4 == "11th president":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")
        
    else:
        print("incroct the answer is (a) 11th president.")
        print("score", score )
        print("\n")
            
            
    # Question 5

    answer5=input ("Q5. who is Abdul Kalam of india ? \n (a) 11th president \n (b) The Messile Man \n (c) Scientist \n (d) Teacher \n Answer :")

    if answer5 == "b" or answer5 == "The Messile Man":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")
        
    else:
        print("incroct the answer is (b) The Messile Man.")
        print("score", score )
        print("\n")
            
            
    # Question 6

    answer6=input ("Q6. what is the age of modi ? \n (a) 54\n (b) 67 \n (c) 71 \n (d) 78 \n Answer :")

    if answer6 == "c" or answer6 == "71":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")
        
    else:
        print("incroct the answer is (c) 71.")
        print("score", score )
        print("\n")
                    
            
    # Question 7

    answer1=input ("Q7. what is Marvel ? \n (a) cartoon \n (b) anime \n (c) movies \n (d) awesome \n Answer :")

    if answer1 == "d" or answer1 == "awesome":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")
        
    else:
        print("incroct the answer is (d) awesome.")
        print("score", score )
        print("\n")
                    
            
    # Question 8

    answer1=input ("Q8. what is Naruto ? \n (a) cartoon \n (b) anime \n (c) movies \n (d) feeling  \n Answer :")

    if answer1 == "d" or answer1 == "feeling":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")
        
    else:
        print("incroct the answer is (d) feeling.")
        print("score", score )
        print("\n")
        
                        
    # Question 9

    answer9=input ("Q9. what is caffeine ? \n (a) energy \n (b) drug \n (c) slow poison \n (d) an alkaloid compound  \n Answer :")

    if answer9 == "d" or answer9 == "an alkaloid compound":
        score = score + 1
        print("correct")
        print("score", score)
        print("\n")
        
    else:
        print("incroct the answer is (d) an alkaloid compound.")
        print("score", score )
        print("\n")
        
        
    # Question 10

    answer1=input ("Q10. what is jorden ? \n (a) shoes \n (b) cloths \n (c) bags \n (d) watch \n Answer :")

    if answer1 == "a" or answer1 == "shoes":
        score = score + 1
        print("correct")
        print("\n")
        print("your total score is", score)
        print("\n")
        
    else:
        print("incroct the answer is (a) shoes.")
        print("\n")
        print("your total score is", score)
        print("\n")
        
    # final massege

    if score <= 3 :
        print("bad ")
    elif score == 5 :
        print("keep learninhg..")
    else :
        print("good job well played...... \n")
    
    num = input ("Do you want to play again? \n (Y) yes \n (N) no) \n Answer: ")