import os
import platform

def shutdown_laptop():
    system_platform = platform.system()

    if system_platform == "Windows":
        os.system("shutdown /s /t 1")
        
    elif system_platform == "Linux" or system_platform == "Darwin":
        os.system("sudo shutdown -h now")
    else:
        print("Unsupported operating system")

def restart_computer():
    system_platform = platform.system()

    if system_platform == "Windows":
        os.system("shutdown /r /t 0")
    elif system_platform == "Linux" or system_platform == "Darwin":
        os.system("sudo reboot")
    else:
        print("Unsupported operating system.")

