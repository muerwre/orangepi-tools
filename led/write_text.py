import os
from display import write, lcd_init;
import requests
import time
from folders import get_uplink_item_count
from format import center

from get_ip import get_lan_ip
from get_ssid import get_ssid
from uplink import get_uplink_status

API_KEY=os.environ.get("API_KEY", "")
API_HOST=os.environ.get("API_HOST", "")
UPLINK_ID=os.environ.get("UPLINK_ID", "")
SCREEN_DELAY=3
INTERFACE="wlan0"

def uplink_status():
    connected = get_uplink_status(API_HOST, API_KEY, UPLINK_ID);
    
    if connected is False:
        return [center("UPLINK OFFLINE"), ""];

    return [center("vault48.org"), center("online")];

def unsync_files():
    count = get_uplink_item_count(API_HOST, API_KEY, UPLINK_ID)
    if count == 0:
        return [center("syncing"), center(f"completed")];
    elif count == -1:
        return [center("syncing"), center(f"## error ##")];
    else:
        return [center("syncing"), center(f"{count} files")];

def get_ip_address():
    ip = get_lan_ip()
    ssid = get_ssid()
    return [center(f"{ip}"), center(f"{ssid}")]

def rand_phrase():
    return [center("Oh, dear,"), center("where am I?")]

screens = [uplink_status, get_ip_address, unsync_files];

if __name__ == '__main__':
    lcd_init();

    if API_KEY == "" or API_HOST == "" or UPLINK_ID == "":
        write(center("you should"), 1);
        write(center("create .env file"), 2);
        exit();

    while (True):
        for fn in screens:
            status = fn();
            write(status[0], 1);
            write(status[1], 2);
            time.sleep(SCREEN_DELAY)