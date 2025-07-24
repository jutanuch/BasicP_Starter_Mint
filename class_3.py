# #for

# number = int(input("enter your number : "))
# for i in range(1,5+1,1):
#     print(i)

# number = int(input("enter your number : "))
# sum = 0
# for i in range(1,number + 1):
#     sum = sum+5
#     print(f"ครั้งที่ {i} ได้ผลเป็น",sum)

# i = 1
# while i <= 5 :
#     print(f"ครั้งที่ {i}")
#     i = i+1

# #workshop
# num = int(input("enter your number : "))
# sum = 0
# i = 1
# while i <= num :
#     sum = sum + 5
#     print(f"ครั้งที่ {i}",sum)
#     i = i+1

#main workshop
mint = 100
Meed = 20
puean = 25
mai = 50

# manu = int(input("enter your num 4 login (1=su,2=mai su) : "))
# if manu == 1:
#     print("ok you su na")
#     times = int(input("how many times you want to su : "))
#     arwut = int(input("do you want a rai su (1= Meed,2= puean,3= mai : ) : "))
#     i = 0
#     while i < times :
#         i = i+1
#         print(i)
#         if arwut == 1 :
#             print("mon hp -20",hp-20)
#     print("mon hp",hp)

    
# else :
#     print("ok mai su kor dai!!")

start = True
while start :
    print("Welcome 2 hehe")
    print("pls enter your num 4 login")
    manu = int(input("enter your num 4 login (1=su,2=mai su) : "))
    if(manu) == 1 :
        times = int(input("how many times you want to su : "))
        for i in range(times):
            print("monster health : ", mint)
            print("1 = Meed ==> 20")
            print("1 = puean ==> 25")
            print("1 = Mai ==> 50")
            print("your attempt", times - i)
            arwat = int(input("choose your arwat: "))
            if arwat == 1 :
                mint _= 20
            elif arwat == 2 :
                mint _= 25 
            elif arwat == 3 :
                mint _= 50
            
            if mint < 0:
                print("capmoocapmeecaphuumadonoi")
                mint = 20
            elif mint == 0:
                print("ca na laeww juuu")
                break
        print("monster health : ",mint)
        if mint == 0:
            print("")
            




