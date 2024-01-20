# Print a hello message
print("Hello, Welcome to my Quiz game!")

# Ask if the user wants to play
choice1 = input('Are you ready to play the Quiz? (yes/no): ')
Score = 0

# Validate user input
if choice1.lower() == 'yes':
    # Ask the first question
    print('Question 1: What programming language have we learned this semester?')
    print('A. Python')
    print('B. SQL')
    print('C. C++')
    print('D. PHP')
    print('E. Malbolge')
    choice2 = input('Please enter your answer: ')

    # Validate user input and update the score
    if choice2.lower() == 'a':
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')
    print('Question 2: How to make a single line comment in Python?')
    print('A. <! -->')
    print('B. /* */')
    print('C. //')
    print('D. -- --')
    print('E. #')
    choice3 = input('Please enter your answer: ')
    if choice3 in ('E', 'e'):
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')

    print('Question 3: What is an IDE?')
    print('A. Internet Developed Eggnog')
    print('B. Iron Development Environment')
    print('C. Integrated Development Environment')
    print('D. Integrated Data Education')
    print('E. Intended Development Education')
    choice4 = input('Please enter your answer: ')
    if choice4 in ('C', 'c'):
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')

    print('Question 4: What is the output of the following code in Python?')
    print('print("Hello World")')
    print('A. Hello World')
    print('B. World Hello')
    print('C. Error')
    print('D. None of the above')
    print('E. Hello')
    choice5 = input('Please enter your answer: ')
    if choice5 in ('A', 'a'):
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')

    print('Question 5: What is the symbol used for assignment in Python?')
    print('A. =')
    print('B. ==')
    print('C. ===')
    print('D. :=')
    print('E. =>')
    choice6 = input('Please enter your answer: ')
    if choice6 in ('A', 'a'):
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')

    print('Question 6: What is a variable in Python?')
    print('A. Value')
    print('B. Container')
    print('C. Method')
    print('D. Loop')
    print('E. Statement')
    choice7 = input('Please enter your answer: ')
    if choice7 in ('B', 'b'):
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')

    print('Question 7: What is the output of the following code?')
    print('print(10 / 2)')
    print('A. 2.0')
    print('B. 5')
    print('C. 2')
    print('D. 5.0')
    print('E. Error')
    choice8 = input('Please enter your answer: ')
    if choice8 in ('D', 'd'):
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')

    print('Question 8: Which of the following is a loop in Python?')
    print('A. do-while')
    print('B. repeat')
    print('C. for')
    print('D. until')
    print('E. foreach')
    choice9 = input('Please enter your answer: ')
    if choice9 in ('C', 'c'):
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')

    print('Question 9: What does the keyword "break" do in Python?')
    print('A. Skips the function')
    print('B. Restarts the function')
    print('C. Executes the function multiple times')
    print('D. Ends the function and returns a value')
    print('E. None of the above')
    choice10 = input('Please enter your answer: ')
    if choice10 in ('D', 'd'):
        Score += 1
        print('Correct!')
    else:
        print('Wrong answer')

# Print a thank you message and display the final score
    print('Thank you for playing this game. You got', Score,'/9 questions correctly!')
elif choice1.lower() == 'no':
    print('Why are you here then? You can\'t play the Quiz.')
else:
    print('Invalid choice. Please enter "yes" or "no".')
    choice1 = input('Are you ready to play the Quiz? (yes/no): ')
    
    if choice1.lower() == 'yes':
        # Ask the first question
        print('Question 1: What programming language have we learned this semester?')
        print('A. Python')
        print('B. SQL')
        print('C. C++')
        print('D. PHP')
        print('E. Malbolge')
        choice2 = input('Please enter your answer: ')

        # Validate user input and update the score
        if choice2.lower() == 'a':
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')
        print('Question 2: How to make a single line comment in Python?')
        print('A. <! -->')
        print('B. /* */')
        print('C. //')
        print('D. -- --')
        print('E. #')
        choice3 = input('Please enter your answer: ')
        if choice3 in ('E', 'e'):
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')

        print('Question 3: What is an IDE?')
        print('A. Internet Developed Eggnog')
        print('B. Iron Development Environment')
        print('C. Integrated Development Environment')
        print('D. Integrated Data Education')
        print('E. Intended Development Education')
        choice4 = input('Please enter your answer: ')
        if choice4 in ('C', 'c'):
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')

        print('Question 4: What is the output of the following code in Python?')
        print('print("Hello World")')
        print('A. Hello World')
        print('B. World Hello')
        print('C. Error')
        print('D. None of the above')
        print('E. Hello')
        choice5 = input('Please enter your answer: ')
        if choice5 in ('A', 'a'):
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')

        print('Question 5: What is the symbol used for assignment in Python?')
        print('A. =')
        print('B. ==')
        print('C. ===')
        print('D. :=')
        print('E. =>')
        choice6 = input('Please enter your answer: ')
        if choice6 in ('A', 'a'):
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')

        print('Question 6: What is a variable in Python?')
        print('A. Value')
        print('B. Container')
        print('C. Method')
        print('D. Loop')
        print('E. Statement')
        choice7 = input('Please enter your answer: ')
        if choice7 in ('B', 'b'):
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')

        print('Question 7: What is the output of the following code?')
        print('print(10 / 2)')
        print('A. 2.0')
        print('B. 5')
        print('C. 2')
        print('D. 5.0')
        print('E. Error')
        choice8 = input('Please enter your answer: ')
        if choice8 in ('D', 'd'):
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')

        print('Question 8: Which of the following is a loop in Python?')
        print('A. do-while')
        print('B. repeat')
        print('C. for')
        print('D. until')
        print('E. foreach')
        choice9 = input('Please enter your answer: ')
        if choice9 in ('C', 'c'):
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')

        print('Question 9: What does the keyword "break" do in Python?')
        print('A. Skips the function')
        print('B. Restarts the function')
        print('C. Executes the function multiple times')
        print('D. Ends the function and returns a value')
        print('E. None of the above')
        choice10 = input('Please enter your answer: ')
        if choice10 in ('D', 'd'):
            Score += 1
            print('Correct!')
        else:
            print('Wrong answer')
    elif choice1.lower() == 'no':
        print('Why are you here then? You can\'t play the Quiz.')