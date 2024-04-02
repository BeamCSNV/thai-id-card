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
mycursor.execute("CREATE TABLE IF NOT EXISTS id_card (id INT AUTO_INCREMENT PRIMARY KEY, identification_number VARCHAR(20), full_name VARCHAR(255), address TEXT)")

# สร้างอินสแตนซ์ของคลาส PersonalCard
reader = PersonalCard(lang="mix", tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract")

# อ่านข้อมูลจากภาพบัตรประชาชน
front_info = reader.extract_front_info("examples/card1.jpg")

# เพิ่มข้อมูลลงในฐานข้อมูล
sql = "INSERT INTO id_card (identification_number, full_name, address) VALUES (%s, %s, %s)"
val = (front_info.Identification_Number, front_info.FullNameTH, front_info.Address)
mycursor.execute(sql, val)
mydb.commit()

print("ข้อมูลบัตรประชาชนถูกเพิ่มลงในฐานข้อมูลแล้ว")
