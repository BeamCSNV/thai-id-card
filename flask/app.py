from flask import Flask, render_template, request
import os
from ThaiPersonalCardExtract import PersonalCard
import mysql.connector

app = Flask(__name__)

# เชื่อมต่อฐานข้อมูล MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="thai-id-card"
)
mycursor = mydb.cursor()

# กำหนดเส้นทางสำหรับหน้าหลัก
@app.route('/')
def home():
    return render_template('index.html')

# กำหนดเส้นทางสำหรับการอัปโหลดรูปภาพ
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)

            # อ่านข้อมูลจากรูปภาพบัตรประชาชน
            reader = PersonalCard(lang="mix", tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract")
            front_info = reader.extract_front_info(file_path)
            back_info = reader.extract_back_info(file_path)

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

            return 'Upload success'
    return 'Upload failed'

# เริ่มการทำงานของเซิร์ฟเวอร์ Flask
if __name__ == '__main__':
    app.run(debug=True)
