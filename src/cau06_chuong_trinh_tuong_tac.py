ma_phien = input("Nhap ma phien:")
ma_may = input("Nhap ma may:")
cong_suat = float(input("Nhap cong suat:"))
so_phut_su_dung = int(input("Nhap so phut su dung:"))
don_gia = int(input("Nhap down gia:"))
dien_nang_kWh = cong_suat * so_phut_su_dung / 60 / 1000
chi_phi = dien_nang_kWh * don_gia
print("Ma phien:",ma_phien)
print("May:",ma_may)
print("Dien nang:",dien_nang_kWh)
print("Chi phi:",chi_phi)