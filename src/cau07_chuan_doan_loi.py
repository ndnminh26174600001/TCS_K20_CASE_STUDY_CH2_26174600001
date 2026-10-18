ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
# Lỗi 1 - SyntaxError dòng 7: thiếu dấu ")" ở cuối print
# File "/home/w/TCS_K20/CASE_STUDY_CH2_MSSV/cau07_chuan_doan_loi.py", line 6
    #print(f"Điện năng: {dien_nang:.3f} kWh"
         #^
#SyntaxError: '(' was never closed
# Lỗi 2 - TypeError dòng 5: input() trả về str nên không chia được
#Traceback (most recent call last):
  #File "/home/w/TCS_K20/CASE_STUDY_CH2_MSSV/cau07_chuan_doan_loi.py", line 4, in <module>
    #dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
                    #~~~~~~~~~~~~~~~~~~~~~~^~~~
#TypeError: unsupported operand type(s) for /: 'str' and 'int'
#Lỗi 3 - NameError dòng 7: gọi sai tên biến dien_nang
#Traceback (most recent call last):
  #File "/home/w/TCS_K20/CASE_STUDY_CH2_MSSV/cau07_chuan_doan_loi.py", line 6, in <module>
    #print(f"Điện năng: {dien_nang:.3f} kWh")
                        #^^^^^^^^^
#NameError: name 'dien_nang' is not defined. Did you mean: 'dien_nang_kwh'?
#Các lỗi ở 1 và 3 đều là các lỗi do cẩu tha mà quên dấu và gọi sai tên biến
#Lỗi 2 do input mặc định gán giá trị str là chuỗi kí tự mà chuỗi kí tự thi không chia được 60 chia được 1000

#Chuong trinh sai
#ma_may input("Nhập mã máy: ")
#cong_suat_w = input("Nhập công suất W: ")
#so_phut = int(input("Nhập số phút: "))
#dien_nang_kwh = cong_suat_w so_phut/60/1000
#print(f'Máy: {ma_may}")
#print (f" Điện năng: (dien_nang:.3f} kWh"
