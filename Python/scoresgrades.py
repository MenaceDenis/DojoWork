print "Scores and Grades"
for i in range(0,10):
    user_input = input('Enter a Score:')
    if user_input < 60:
        print "Score: ", user_input,"; Your grade is an F"
    elif user_input <= 69:
        print "Score: ", user_input,"; Your grade is an D"
    elif user_input <= 79:
        print "Score: ", user_input,"; Your grade is an C"
    elif user_input <= 89:
        print "Score: ", user_input,"; Your grade is an B"
    elif user_input <= 100:
        print "Your grade is an A" #anything less than 60 could be A.
