import sys
from ThaiPersonalCardExtract import PersonalCard

if len(sys.argv) < 2:
    print("กรุณาใส่ที่อยู่ของไฟล์รูปภาพ")
    sys.exit(1)

img_path = sys.argv[1]

reader = PersonalCard(lang="mix", tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract")

front_info = reader.extract_front_info(img_path)
print("ข้อมูลบัตร:\n")

print("เลขบัตรประจำตัว:", front_info)
# print("ชื่อเต็ม (ไทย):", front_info.FullNameTH)
# print("คำนำหน้าชื่อ (ไทย):", front_info.PrefixTH)
# print("ชื่อ (ไทย):", front_info.NameTH)
# print("นามสกุล (ไทย):", front_info.LastNameTH)
# print("คำนำหน้าชื่อ (อังกฤษ):", front_info.PrefixEN)
# print("ชื่อ (อังกฤษ):", front_info.NameEN)
# print("นามสกุล (อังกฤษ):", front_info.LastNameEN)
# print("วันเดือนปีเกิด (ไทย):", front_info.BirthdayTH)
# print("วันเดือนปีเกิด (อังกฤษ):", front_info.BirthdayEN)
# print("ศาสนา:", front_info.Religion)
# print("ที่อยู่:", front_info.Address)
# print("วันที่ออกบัตร (ไทย):", front_info.DateOfIssueTH)
# print("วันที่ออกบัตร (อังกฤษ):", front_info.DateOfIssueEN)
# print("วันที่หมดอายุ (ไทย):", front_info.DateOfExpiryTH)
# print("วันที่หมดอายุ (อังกฤษ):", front_info.DateOfExpiryEN)
# print("รหัสเลเซอร์:", front_info.LaserCode)
