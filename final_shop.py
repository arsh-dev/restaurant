d={ "1": "Pizza - 50rs",
    "2": "Burger - 40rs",
    "3": "Maggie - 30rs",
    "4": "Paties - 20rs"}
for i in d:
    print(i+')', d[i])

print()
final=[]

l1=[0,1,2,3,4]
l2=["Thank you","Pizza","Burger","Maggie","Paties"]
price=[0,50,40,30,20]

p=1
while p>0:
    t=int(input("Enter your Table Number: "))
    x=int(input("Enter Dish Number: "))
    for i in l1:
        if x>0:
            if i==x:
                a=(l2[i])
                print(a)
                final.append(a)
                print("Nice Choice! ")
        else:
            break
    print()
    for i in range(10):
        y=int(input("If you want something else, enter dish number, else enter 0.\nPlease enter here: "))
        if y!=0:
            for i in l1:
                if (i==y) :
                    b=(l2[i])
                    print(b)
                    final.append(b)
        else:
            break
    if len(final)>0:    
        print("your items are : ",final)
    else:
        print("You haven't ordered anything!")

    fp=[]
    bill=[]
    for i in final:
        for j in l2:
            if i==j:
                q=l2.index(j)
                fp.append(q)
#print(fp)
    for i in fp:
        w=price[i]
        bill.append(w)
    
#print(bill)

    sum=0
    for i in bill:
        sum+=i
    print("Your Bill for table number ",int(t),'is:  ', sum ,'rs')
    print("Glad to serve you, COME AGAIN !")
    print()


