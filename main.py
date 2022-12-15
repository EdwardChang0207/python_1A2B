#import moudles
import random as r
#spawn answer
ans = []
while len(ans) <= 3:
    index = r.randint(1, 9) #spawn 4 random values between 1~9
    if not ans.count(index): #pervent from a value appears twice
        ans.append(index)
    else:
        continue
#print(ans)
correct = False
while not correct:
    #get user's input value
    user_input = [int(i) for i in input().split()]
    #check answer
    a = 0
    b = 0
    for i in range(len(ans)): #check if there's same values in two lists
        for j in range(len(user_input)):
            if user_input[j] == ans[i]:#if the value's position is equla in both lists
                if j == i: #increase A
                    a += 1
                else: #increase B
                    b += 1
    print(str(user_input)+", "+str(a)+"A"+str(b)+"B") #print the result of each input
    if a == 4: #if 4A => game clear
        print("PASS")
        correct = True #stop the while loop in line 13
