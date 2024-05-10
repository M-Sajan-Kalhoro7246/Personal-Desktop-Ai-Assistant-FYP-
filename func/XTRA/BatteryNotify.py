
from plyer import notification 
import psutil
from time import sleep

def battery():
    battery = psutil.sensors_battery()
    life = battery.percent
    plugged = battery.power_plugged
    plugged = "Plugged In" if plugged else "Powe Souce Not Plugged In"
    if life < 30:
        notification.notify(
            title = "Battery Saving On Sir",
            message ="Sir Please Connect to a Power Source",
            timeout = 10
        )
    print('Battery Low',f'{life}%',plugged)   
    sleep(20)

def cpu():
    life = str(psutil.cpu_percent())
    print("CPU is at "+life)
    battery = psutil.sensors_battery().percent
    print(f"Battery is at ",battery)
cpu()