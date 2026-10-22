chuoi_nhap = input("nhap chuoi so :")
chuoi_so=[float (x) for x in chuoi_nhap.split()]
print ("chuoi da nhap :",(chuoi_so))
tong = sum(chuoi_so)
N = len(chuoi_so)
trung_binh = tong/N
print ("trung binh cong cua",(chuoi_so),"la :",(trung_binh))
tong_trung_binh=  sum((i-trung_binh)**2  for i in (chuoi_so)) #cach su dung sum va list 
print ("tong binh phuong cua",(chuoi_so),"la :",(tong_trung_binh))