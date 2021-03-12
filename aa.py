import os
import time

# checking for connected devices
print("Stability test has been completed.")
print("Android logs and Kernel log has been generated in the workspace.")
device = os.popen("adb devices").read()
print(device)

# connect to the selected device 172.0.0.1:62001

connect = os.popen("adb connect "+device).read()
#print(connect)

# gradle build apk and install apk
os.system("./gradlew clean installDebug ")

#testing and collecting logcat

os.system("adb shell monkey -v --throttle 100 -p com.example.myapplication 1000 > test11log.txt")
time.sleep((1000*100)/1000)

#kernel log
os.popen("adb shell dmesg >kernel3log.txt")
print("hello CTS")
