import os

def get_ssid():
  try:
    ssid = os.popen("sudo iwgetid -r").read()
    return ssid;
  except:
    return "(unknown)"