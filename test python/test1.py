from ThaiPersonalCardExtract import PersonalCard

reader = PersonalCard(lang="mix", tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract")

# สำหรับตรวจจับภาพด้านหน้าบัตร
front_info = reader.extract_front_info(r"examples\card1.jpg")
print("ข้อมูลบัตรที่ 1:\n")

print("เลขบัตรประจำตัว:", front_info.Identification_Number)
print("ชื่อเต็ม (ไทย):", front_info.FullNameTH)
print("คำนำหน้าชื่อ (ไทย):", front_info.PrefixTH)
print("ชื่อ (ไทย):", front_info.NameTH)
print("นามสกุล (ไทย):", front_info.LastNameTH)
print("คำนำหน้าชื่อ (อังกฤษ):", front_info.PrefixEN)
print("ชื่อ (อังกฤษ):", front_info.NameEN)
print("นามสกุล (อังกฤษ):", front_info.LastNameEN)
print("วันเดือนปีเกิด (ไทย):", front_info.BirthdayTH)
print("วันเดือนปีเกิด (อังกฤษ):", front_info.BirthdayEN)
print("ศาสนา:", front_info.Religion)
print("ที่อยู่:", front_info.Address)
print("วันที่ออกบัตร (ไทย):", front_info.DateOfIssueTH)
print("วันที่ออกบัตร (อังกฤษ):", front_info.DateOfIssueEN)
print("วันที่หมดอายุ (ไทย):", front_info.DateOfExpiryTH)
print("วันที่หมดอายุ (อังกฤษ):", front_info.DateOfExpiryEN)
print("รหัสเลเซอร์:", front_info.LaserCode)
print()

# และด้านหลังบัตร
back_info = reader.extract_back_info(r"examples\card5.jpg")
print("ข้อมูลบัตรที่ 2:\n")

print("เลขบัตรประจำตัว:", back_info.Identification_Number)
print("ข้อมูลอื่น ๆ ก็เหมือนกับบัตรที่ 1 แต่มีรหัสเลเซอร์:", back_info.LaserCode)
