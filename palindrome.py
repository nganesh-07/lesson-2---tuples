def palindrome(r):
    e = len(r)-1
    s = 0
    while(s<e):
        if(r[s]!= r[e]):
            return False
        s+=1
        e-=1
    return True

r = input("Enter any text palindrome here:")

if palindrome(r):
    print("The tuple is a flip-flop")
else:
    print("The tuple is not a flip-flop")