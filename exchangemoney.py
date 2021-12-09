import math
# doi tien viet sang tien do
usd = float(input("Nhập vào số USD cần đổi: "))
Exchangerate = float(input("Tỉ giá hiện tại"))
print("Tiền VND quy đổi: " + str(Exchangerate*usd))

# doi do sang viet
dollar = float(input('Nhap vao so tien can chuyen doi: '))
vnd = dollar*22930.00
print("Gia tien khi chuyen doi la: " + str(vnd))
