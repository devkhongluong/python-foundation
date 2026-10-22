#nhuận khi chia hết cho 4 nhưng k chia hết cho 100
y = input ("vui lòng nhập số năm " )
y = int (y)
if ( y%4==0 and y%100!=0):
    print ((y),"là năm nhuận")
elif(y%400==0):
    print ((y),"là năm nhuận")
else:
    print ((y),"không phải năm nhuận")