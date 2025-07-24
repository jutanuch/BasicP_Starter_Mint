#function return คำนวณเกรดออกมา

# def grade(score):
#     if score >= 50 :
#         print("your passed")
#         if score >= 80 :
#             print("Grade A")
#         elif score >= 70 :
#             print("Grade B")
#         elif score >= 60 :
#             print("Grade C")
#         else :
#             print("Grade D")
#     else :
#         print("your fail")
# grade(70)

def koon(x, y) :
    for i in range(1, y+1) :
        print(f"{x} * {i} = {x*i}")
    
koon(2, 12)
    
