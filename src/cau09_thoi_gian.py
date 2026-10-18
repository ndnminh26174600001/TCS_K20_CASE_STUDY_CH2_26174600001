from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
#dự đoán phép trừ: 15:05 - 13:15 = 1 giờ 50 phút = 1:50:00
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))
#datetime là mốc thời gian (ngày + giờ), có thể tính toán, so sánh.
#str là chuỗi văn bản chỉ để hiển thị, không trừ hay so sánh thời gian được.
#timedelta là khoảng thời gian, kết quả của phép trừ hai datetime