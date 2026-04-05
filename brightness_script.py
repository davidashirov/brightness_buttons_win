import winreg
import win32event
import win32api
import monitorcontrol
from datetime import datetime

def set_brightness(value):
    monitors = monitorcontrol.get_monitors()
    with monitors[0]:
        monitors[0].set_contrast(value)
        monitors[0].set_luminance(value)
    
def decide_brightness_startup():
    """ Check time and output brightness appropriate for the time of day"""
    now = datetime.now().time()
    if now >= datetime.strptime("06:00", "%H:%M").time() and now < datetime.strptime("20:00", "%H:%M").time():
        return 100
    else:
        return 10
        
def monitor_registry_changes():
    key_path = r"SYSTEM\CurrentControlSet\Control\Power\User\PowerSchemes\8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c\7516b95f-f776-4464-8c53-06167f40cc99\aded5e82-b909-4619-9949-f5d71dac0bcb"
    
    # Open the registry key
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ)
    
    # Create an event object
    event = win32event.CreateEvent(None, False, False, None)
    
    print("Monitoring registry changes...")
    
    try:
        while True:
            # Register for change notifications
            win32api.RegNotifyChangeKeyValue(key, True, winreg.REG_NOTIFY_CHANGE_NAME | winreg.REG_NOTIFY_CHANGE_LAST_SET, event, True)
            
            # Wait for the event to be signaled
            win32event.WaitForSingleObject(event, win32event.INFINITE)
            print("Registry key changed!")
            
            # Read and print the value (replace "ValueName" with actual value name)
            value, _ = winreg.QueryValueEx(key, "ACSettingIndex")  # or "DCSettingIndex"
            print(f"Current value: {value}")
            set_brightness(value)
            
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    finally:
        winreg.CloseKey(key)

if __name__ == "__main__":
    brightness_startup = decide_brightness_startup()
    set_brightness(brightness_startup)
    monitor_registry_changes()