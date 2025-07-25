# def booking_system():
#     # เริ่มต้น
#     general_zone_available = 4
#     private_zone_available = 4

#     print("แสดงที่นั่ง")
#     print(f"โซน general ว่าง : {general_zone_available}")
#     print(f"โซน private ว่าง : {private_zone_available}")
    
#     print("choose zone")
#     zone = input("กรุณาเลือกโซน (พิมพ์ 'general' หรือ 'private'): ").strip().lower()
    
#     if zone == "general":
#         print("you choose gen")
#     elif zone == "private":
#         print("you choose private")
#     else:
#         print("คุณเลือกโซนไม่ถูกต้อง")
#         return

#     print("choose num of table")
#     num_table = input("กรอกจำนวนโต๊ะที่ต้องการ: ")
#     print(f"num of table: {num_table}")

#     print("choose time for booking")
#     booking_time = input("กรอกเวลาที่ต้องการจอง (เช่น 18:00): ")
#     print(f"time for booking: {booking_time}")

#     print("how many hr you want to play")
#     hr_play = input("กรอกจำนวนชั่วโมงที่ต้องการเล่น: ")
#     print(f"hr of playing: {hr_play}")

#     print("how many people")
#     num_people = input("กรอกจำนวนคน: ")
#     print(f"number of people: {num_people}")

#     print("confirm your booking")
#     print("\n--- รายละเอียดการจอง ---")
#     print(f"โซนที่เลือก: {zone}")
#     print(f"จำนวนโต๊ะ: {num_table}")
#     print(f"เวลาเริ่มต้น: {booking_time}")
#     print(f"จำนวนชั่วโมงที่เล่น: {hr_play}")
#     print(f"จำนวนคน: {num_people}")
#     print("ขอบคุณที่ใช้บริการจองโต๊ะ!")

# # เรียกใช้ฟังก์ชัน
# booking_system()


# กำหนดจำนวนโต๊ะเริ่มต้นในแต่ละโซน
available_tables = {
    "general": 4,
    "private": 4
}

def booking_system():
    print("แสดงที่นั่ง")
    print(f"โซน general ว่าง : {available_tables['general']}")
    print(f"โซน private ว่าง : {available_tables['private']}")
    
    # เลือกโซน
    print("choose zone")
    zone = input("กรุณาเลือกโซน (พิมพ์ 'general' หรือ 'private'): ").strip().lower()

    if zone not in available_tables:
        print("คุณเลือกโซนไม่ถูกต้อง")
        return
    
    print(f"you choose {zone}")
    
    # เลือกจำนวนโต๊ะ
    print("choose num of table")
    try:
        num_table = int(input("กรอกจำนวนโต๊ะที่ต้องการ: "))
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น")
        return

    if num_table <= 0:
        print("จำนวนโต๊ะต้องมากกว่า 0")
        return

    if num_table > available_tables[zone]:
        print(f"ขออภัย โต๊ะในโซน {zone} เหลือเพียง {available_tables[zone]} โต๊ะเท่านั้น")
        return
    else:
        print(f"num of table: {num_table}")
    
    # กรอกเวลาจอง
    print("choose time for booking")
    booking_time = input("กรอกเวลาที่ต้องการจอง (เช่น 18:00): ")
    print(f"time for booking: {booking_time}")

    # จำนวนชั่วโมงที่เล่น
    print("how many hr you want to play")
    hr_play = input("กรอกจำนวนชั่วโมงที่ต้องการเล่น: ")
    print(f"hr of playing: {hr_play}")

    # จำนวนคน
    print("how many people")
    num_people = input("กรอกจำนวนคน: ")
    print(f"number of people: {num_people}")

    # ลดจำนวนโต๊ะในโซนที่จอง
    available_tables[zone] -= num_table

    # ยืนยันการจอง
    print("\n✅ ยืนยันการจอง")
    print(f"โซนที่เลือก: {zone}")
    print(f"จำนวนโต๊ะ: {num_table}")
    print(f"เวลาเริ่มต้น: {booking_time}")
    print(f"จำนวนชั่วโมงที่เล่น: {hr_play}")
    print(f"จำนวนคน: {num_people}")
    print("📌 ขอบคุณที่ใช้บริการจองโต๊ะ!")

# เรียกใช้ระบบจองหลายครั้งเพื่อทดสอบว่าโต๊ะลดจริง
while True:
    booking_system()
    again = input("\nคุณต้องการจองอีกหรือไม่? (y/n): ").strip().lower()
    if again != 'y':
        break
