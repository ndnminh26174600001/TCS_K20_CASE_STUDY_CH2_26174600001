from datetime import datetime
ma_phien = input("Nhap ma phien:")
ma_may = input("Nhap ma may:")
cong_suat_thiet_bi_w = float(input("Nhap cong suat thiet bi (w):"))
thoi_gian_su_dung_phut = int(input("Nhap thoi gian su dung (phut):"))
don_gia_dien_VND_kWh = float(input("Nhap don gia dien (VND/kWh):"))
dien_nang_tieu_thu = thoi_gian_su_dung_phut * cong_suat_thiet_bi_w /60/1000
chi_phi = dien_nang_tieu_thu * don_gia_dien_VND_kWh
su_dung_tren_60_phut = thoi_gian_su_dung_phut > 60
ghi_nhan_luc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Ma phien:{ma_phien}")
print(f"Ma may:{ma_may}")
print(f"Cong suat:{cong_suat_thiet_bi_w:.2f}W")
print(f"Thoi luong:{thoi_gian_su_dung_phut}phut")
print(f"Dien nang:{dien_nang_tieu_thu:.3f}W")
print(f"Chi phi:{chi_phi:.2f}VND")
print(f"Tren 60 phut:{su_dung_tren_60_phut}")
print(f"Ghi nhan luc:{ghi_nhan_luc}")