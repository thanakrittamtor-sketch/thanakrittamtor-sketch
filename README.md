# 🐍 My Portfolio (Python + Flask)

เว็บไซต์ Portfolio ส่วนตัว สร้างด้วย Python (Flask) แสดงข้อมูลส่วนตัว ทักษะ ผลงาน และช่องทางติดต่อ

## ✨ Features
- หน้า Landing พร้อม Hero Section
- ส่วนแสดงทักษะ (Skills)
- ส่วนแสดงผลงาน (Projects) แบบ Card
- ส่วนติดต่อ (Contact)
- ดีไซน์ Responsive รองรับมือถือ

## 🛠 เทคโนโลยีที่ใช้
- Python 3
- Flask
- HTML / CSS (Jinja2 Template)

## 🚀 วิธีติดตั้งและรัน

```bash
# 1. Clone โปรเจกต์
git clone https://github.com/yourusername/portfolio.git
cd portfolio

# 2. สร้าง virtual environment (แนะนำ)
python -m venv venv
source venv/bin/activate      # บน Windows ใช้: venv\Scripts\activate

# 3. ติดตั้ง dependencies
pip install -r requirements.txt

# 4. รันเว็บไซต์
python app.py
```

จากนั้นเปิดเบราว์เซอร์ไปที่ `http://127.0.0.1:5000`

## ✏️ การปรับแต่ง
แก้ไขข้อมูลส่วนตัว ทักษะ และผลงานได้ที่ไฟล์ `app.py` ในตัวแปร `profile`, `skills`, และ `projects`

## 📁 โครงสร้างโปรเจกต์
```
portfolio/
├── app.py                 # โค้ดหลัก Flask + ข้อมูล
├── requirements.txt       # รายการ dependencies
├── templates/
│   └── index.html         # หน้าเว็บหลัก
└── static/
    └── css/
        └── style.css       # สไตล์ของเว็บไซต์
```

## 📄 License
MIT License — ใช้และดัดแปลงได้อย่างอิสระ
