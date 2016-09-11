x = [4,6,1,3,5,7,25]

for idx in range(0, len(x)): #'we will do this so many times, from 0 to the lenght of the list'
    stars = '' # everytime the outter for lop changes values, fro 4 to 6 to 1 the stars function will fire. this is an empty string. we built it up.
    for num in range(0,x[idx]): #nested for loop. the x[idx] will be placed by 4,6,1,3...down the line. "tack on a star from 0-4 but not including 4"
        stars += '*'
    print stars
        #print '*', #prints the number of starts the correspond to the range, x[idx]. adding the comma put the * on the same line
    #print x[idx] #looks into the x list. looks at the different index postions


for idx in range(0, len(x)): #another option to do this
    print x[idx] * '4'
