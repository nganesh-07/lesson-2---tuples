weather = (1, 0, 0, 1, 0, 0, 1, 1, 1, 1)
sunny = 0
rainy = 0
for i in range(0,10):
    if weather[i]==0:
        rainy +=1
    else:
        sunny +=1

if sunny>rainy:
    print("good weather!")
else:
    print("bad weather...")