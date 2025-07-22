# x = int(input("enter number 1: "))
# y = int(input("enter number 2: "))

# if x > y :
#     print("x>y")
#     print(x*y)
# elif x < y :
#     print("x<y")
#     print(x/y)
# elif x == y :
#     print("x=y")
#     print(x+y)
# else :
#     print("idk")


x = int(input("enter your distance(km): "))
price = 0
if x >= 5 and x <= 50 : 
    print("your price is 10 bath")
    price = 10
elif x >= 51 and x <= 100 :
    print("your price is 15 bath")
    price = 15
elif x >= 101 and x <= 300 :
    print("your price is 25 bath")
    price = 25
elif x >= 301 and x <= 500:
    print("your price is 35 bath")
    price = 35
elif x >500 :
    print("your price is 45 bath")
    price = 45

vat = int(price*7/100)
result = price+vat
if x <4 :
    print("your price is free bath")
else :
    print(vat)
    print("your final price is", result)





