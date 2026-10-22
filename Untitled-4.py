#f=c1.8 +32, c= (F-32)/1.8
i= input("vui lòng xác nhận chọn đổi từ độ C hay độ f :")
if (i=="c"):
    c=input("vui lòng nhập nhiệt độ C")
    c=float(c)
    kq=c*1.8+32
    print("nhiệt độ F=",(kq))
elif(i=="f"):
    F= input("vui lòng nhập nhiệt độ F")
    F=float(F)
    kq=(F-32)/1.8
    print("nhiệt độ C =",(kq))
else:
    print("bảng quy đổi C ->F (0->100c)")
    for i in range(101):
        kq=i*1.8 +32;
        print ("c =",(i),"F = ",(kq))
    
