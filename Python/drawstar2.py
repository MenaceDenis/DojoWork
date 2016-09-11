y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

for idx in range(0, len(y)):
    if isinstance(y[idx], str): #this will grab all the values, 4, tom, 1,....type tells you what type of chartacter this is. intiger or string.i think this code will grab the string.
        strlen = len(y[idx])
        print strlen * y[idx][0].lower() #grabs first chartacter
    else:
        print y[idx] * '*'
