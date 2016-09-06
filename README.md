# loginSpy

A python script to send sms to your mobile phone whenever someone login into your Ubuntu/Linux system

![loginSpy-Screenshot](https://cloud.githubusercontent.com/assets/12946753/18292530/4a880584-74ab-11e6-945d-f4b692af5595.png)

This script sends the sms to Indian mobile number only using [way2sms](www.way2sms.com). If you are from India, create a free account and feed your username (mobile number) and password into the script under the ```sendsms``` method. 

## Building the executable and running the script at bootup

1. Install ```PyInstaller``` using the command ```sudo pip install PyInstaller```
2. Make the executable using the command ```pyinstaller --onefile loginSpy.py```
3. Search for ```Startup Applications``` in the unity and add the path of executable to it ( found under ```loginSpy/dist```) 
