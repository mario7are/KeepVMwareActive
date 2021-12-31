import os
import subprocess

import pyautogui
from AppKit import NSScreen, NSDeviceSize, NSWorkspace

if __name__ == '__main__':
    vmware = "VMware Horizon Client"
    cmd = """
    tell application "System Events" to tell process "VMware Horizon Client"
    set frontmost to true
	windows where title contains "mspv-"
	    if result is not {} then
	        perform action "AXRaise" of item 1 of result
            key code 124
            key code 123
	    end if
    end tell
    """
    tmp = os.popen("ps -Af").read()
    active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
    if vmware in tmp[:]:
        acumulated = 0
        mouse_x, mouse_y = pyautogui.position()
        for i, screen in enumerate(NSScreen.screens(), 1):
            description = screen.deviceDescription()
            scaleFactor = screen.backingScaleFactor()
            screen_x, screen_y = description[NSDeviceSize].sizeValue()
            acumulated += screen_x - 1
            screen_center_x = acumulated - (screen_x / 2)
            screen_center_y = screen_y / 2
            pyautogui.moveTo(acumulated, screen_center_y)
            result = subprocess.run(['osascript', '-e', cmd], capture_output=True)
            if result.returncode > 0:
                print(result)
        if mouse_x == 0 and mouse_y == 0:
            mouse_x = 1
            mouse_y = 1

        pyautogui.moveTo(mouse_x, mouse_y)

        previousApp = "tell application " + "\"" + active_app_name + "\" " + " to Activate"
        subprocess.run(['osascript', '-e', previousApp], capture_output=True)
