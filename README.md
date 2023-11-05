# Keylogger
**Keyboard gestures, Send screenshots to your mail. The aim of the project is to test the security of information systems**


## Requirements
* **`pip install pyautogui`**<br/>
* **`pip install pynput`**<br/>
* **`pip install zipfile`**
* **`pip install pyinstaller`**



## Create An Application Password
* **You need to turn on `two-step verification` from the generated email address.**
* **You need to create an `application password` from your mail**
* **You can get a `temporary email address` for this process from some sites.**

```bash
sender_email = "yourmail@example.com"
sender_password = "your application password"
```

  
## Create Exe File

```bash
 pip install pyinstaller
 pyinstaller --onedir --noconsole keyLogger.py
```


## Start Keylogger
**If you want to run the application in the code editor and not as an exe file, fix these codes.These and similar.**

```bash
log = open("..\\..\\Logs\\log.txt", "w") => log = open("Logs\\log.txt", "w")
zip_name=f"..\\..\\Rar Files\\Log{zip_counter}.zip" => zip_name=f"Rar Files\\Log{zip_counter}.zip"
```

<br>

## System's Logic
* **Every 20 seconds while the application is running, it takes an image of the screen and stores it under the Images folder.**
* **Every key pressed by the user is instantly recorded in a text file under Logs.**
  
  <img src="https://github.com/Efe-Eroglu/Keylogger/assets/95614657/c61365ad-65f0-4a29-9c7c-ed5c91514654" width="200" height="250" alt="dosya_yapisi" align="center">


* **Every 10 minutes these recordings are zip-ed and sent to your e-mail address.**

     <img src="https://github.com/Efe-Eroglu/Keylogger/assets/95614657/209be968-9e21-4a49-9222-ed4b0c091ffa" alt="mail_log">

## Note
* **This application has been prepared within the scope of information system security course. It is not suitable for malicious use and its use for such purposes is strictly prohibited and not recommended.**
