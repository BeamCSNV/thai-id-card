import mysql.connector
from ThaiPersonalCardExtract import PersonalCard

# เชื่อมต่อฐานข้อมูล MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="thai-id-card"
)
mycursor = mydb.cursor()

# สร้างตารางเพื่อเก็บข้อมูลบัตรประชาชน
mycursor.execute("CREATE TABLE IF NOT EXISTS id_card (id INT AUTO_INCREMENT PRIMARY KEY, identification_number VARCHAR(20), full_name VARCHAR(255), prefix_th VARCHAR(50), name_th VARCHAR(100), last_name_th VARCHAR(100), prefix_en VARCHAR(50), name_en VARCHAR(100), last_name_en VARCHAR(100), birthday_th VARCHAR(50), birthday_en VARCHAR(50), religion VARCHAR(50), address TEXT, date_of_issue_th VARCHAR(50), date_of_issue_en VARCHAR(50), date_of_expiry_th VARCHAR(50), date_of_expiry_en VARCHAR(50), laser_code VARCHAR(50))")

# สร้างอินสแตนซ์ของคลาส PersonalCard
reader = PersonalCard(lang="mix", tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract")

# อ่านข้อมูลจากภาพบัตรประชาชน
front_info = reader.extract_front_info("examples/card1.jpg")
back_info = reader.extract_back_info("examples/card5.jpg")

# เพิ่มข้อมูลลงในฐานข้อมูล
sql = "INSERT INTO id_card (identification_number, full_name, prefix_th, name_th, last_name_th, prefix_en, name_en, last_name_en, birthday_th, birthday_en, religion, address, date_of_issue_th, date_of_issue_en, date_of_expiry_th, date_of_expiry_en, laser_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (
    front_info.Identification_Number, front_info.FullNameTH, front_info.PrefixTH, front_info.NameTH, front_info.LastNameTH,
    front_info.PrefixEN, front_info.NameEN, front_info.LastNameEN, front_info.BirthdayTH, front_info.BirthdayEN,
    front_info.Religion, front_info.Address, front_info.DateOfIssueTH, front_info.DateOfIssueEN,
    front_info.DateOfExpiryTH, front_info.DateOfExpiryEN, front_info.LaserCode
)
mycursor.execute(sql, val)

val = (
    back_info.Identification_Number, back_info.FullNameTH, back_info.PrefixTH, back_info.NameTH, back_info.LastNameTH,
    back_info.PrefixEN, back_info.NameEN, back_info.LastNameEN, back_info.BirthdayTH, back_info.BirthdayEN,
    back_info.Religion, back_info.Address, back_info.DateOfIssueTH, back_info.DateOfIssueEN,
    back_info.DateOfExpiryTH, back_info.DateOfExpiryEN, back_info.LaserCode
)
mycursor.execute(sql, val)

mydb.commit()

print("ข้อมูลบัตรประชาชนถูกเพิ่มลงในฐานข้อมูลแล้ว")
