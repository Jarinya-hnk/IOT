# s01_buddy.py - Buddy Challenge ข้อ 1: จอต้อนรับของทีม
#
# โจทย์: หน้าจอต้อนรับที่มี หัวเรื่อง + ชื่อทีม + คำขวัญ + รายชื่อสมาชิกพร้อมหน้าที่ในทีม
#        ใช้สีต่างกันระหว่างหัวเรื่องกับเนื้อหา
#
# วิธีรัน: แตะการ์ด Playground บนหน้า Home ก่อน แล้วกด Program to Device

import lcd
import time
import ui

# ---------- แก้ให้เป็นของทีมจริงก่อนส่งขึ้นบอร์ด ----------
TEAM_NAME = "Group13"
MOTTO = "รักที่ดีคือรักสบู่"

# แต่ละคนคือ (ชื่อ, หน้าที่ในทีม) — TODO: แก้เป็นชื่อและหน้าที่จริงของสมาชิก
MEMBERS = [
    ("จริญญา", "Driver"),
    ("สุภัสสร", "Navigator"),
    ("ธนดล", "Recorder/Testter"),
]

# จานสี - แยกบทบาทชัดเจน: หัวเรื่องเด่น เนื้อหาอ่านง่าย ไม่แย่งกัน
COL_HEADER = 0x4A9EFF   # สีฟ้าเน้น - ใช้กับหัวเรื่องและชื่อทีมเท่านั้น
COL_TEXT = 0xE8EAED     # สีขาวเนื้อหาหลัก - คำขวัญ, ชื่อสมาชิก
COL_DIM = 0x9AA3AF      # สีเทาจาง - ป้ายกำกับ, หน้าที่ในทีม
COL_CARD = 0x171B22     # พื้นการ์ด

ui.screen()
time.sleep_ms(200)

# การ์ดหลักครอบทุกอย่าง ให้จอต้อนรับดูเป็นชิ้นเดียว ไม่ใช่ตัวหนังสือลอย ๆ
ui.Panel(x=16, y=8, w=760, h=372, color=COL_CARD, min=COL_DIM, max=12, value=1)

# --- หัวเรื่อง (สีเน้น ต่างจากเนื้อหา) ---
ui.Label("AIoT in Action - คาบ 1", x=32, y=20, color=COL_HEADER, value=22)

# --- ชื่อทีม (ใช้สีเน้นเดียวกับหัวเรื่อง เพราะเป็นของที่อยากให้เด่นสุด) ---
ui.Label(TEAM_NAME, x=32, y=56, color=COL_HEADER, value=32)

# --- คำขวัญ (สีเนื้อหาปกติ ไม่ใช่สีเน้น) ---
ui.Label(MOTTO, x=32, y=104, color=COL_TEXT, value=20)

# --- หัวข้อย่อยก่อนรายชื่อสมาชิก ---
ui.Label("สมาชิกในทีม", x=32, y=148, color=COL_DIM, value=18)

# --- รายชื่อสมาชิกพร้อมหน้าที่ ไล่ทีละแถว ---
y = 176
for name, role in MEMBERS:
    ui.Label(name, x=48, y=y, color=COL_TEXT, value=20)
    ui.Label(role, x=280, y=y, color=COL_DIM, value=20)
    ui.poll()
    time.sleep_ms(300)
    y += 40

ui.poll()

# ปิดท้ายในลิ้นชัก Console ด้วย เผื่อใครไม่ทันมองหน้า Playground
lcd.clear()
lcd.console("<h2>AIoT in Action - คาบ 1</h2>")
lcd.print("<span class=ok>ทีม " + TEAM_NAME + " พร้อมแล้ว</span>")

print("จอต้อนรับของทีม " + TEAM_NAME + " ขึ้นจอแล้ว")
