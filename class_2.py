# # x = int(input("enter your grade: "))
# # if x > 50 :
# #     print("your pass")
# #     if x>= 80 :
# #         print("your grade A")
# #     elif x>= 70 :
# #         print("your grade B")
# #     elif x>= 60 :
# #         print("your grade C")
# #     elif x >= 50 :
# #         print("your grade D")
# # else :
# #     print("your fail")
   

user = input("enter your type : ")
price = int(input("enter your price : "))
date = int(input("enter your date : "))

if user == "gold" :
    if price >= 1000 :
        print("get discont 15%")
    else :
        print("get discont 10%")

elif user == "silver" :
    if price >= 1000 :
        print("get discont 10%")
    else :
        print("get discont 5%")
else :
    print("no discont for you")

# ทำโปร

if date%2 != 0 :
    print("get 500 bath")

#คำนวณ

result = price

