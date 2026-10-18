cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
#Du doan gia tri va kieu du lieu cua hai ket qua
#dien_nang_kwh = 0.375 kieu float
#chi_phi = 1125.0 kieu float
print("Dien nang(kwh):",dien_nang_kwh,type(dien_nang_kwh))
print("Chi phi(dong):",chi_phi,type(chi_phi))
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Dien nang(kwh):",dien_nang_kwh,type(dien_nang_kwh))
print("Chi phi(dong):",chi_phi,type(chi_phi))
#thời gian giảm từ 90 xuống 60 phút thì điện năng và chi phí giảm theo tỉ lệ (0.375 → 0.25, 1125 → 750), kiểu dữ liệu vẫn là float