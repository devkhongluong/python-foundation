can_nang=input("vui lòng nhập số cân nặng của bạn ")
chieu_cao=input("vui lòng nhập chiều cao của bạn ")
chieu_cao=float(chieu_cao)
can_nang=float(can_nang)
BMI = can_nang/(chieu_cao*chieu_cao)
if (BMI<18.5):
    print("bạn đang thiếu cân") 
if (BMI>=18.5 and BMI <25):
    print ("bạn đang bình thường")
if (BMI >=25 and BMI <30):
    print("bạn đang thừa cân")
if (BMI >=30):
    print("bạn đang béo phì")


