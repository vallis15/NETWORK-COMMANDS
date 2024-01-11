import subprocess
import os

def ping_test(address):
    cmd = 'ping ' + address
    subprocess.call(['osascript', '-e', 'tell application "Terminal" to do script "{}"'.format(cmd)])

def traceroute_test(address):
    cmd = 'traceroute ' + address
    subprocess.call(['osascript', '-e', 'tell application "Terminal" to do script "{}"'.format(cmd)])

def show_curl(address):
    cmd = 'curl ' + address
    subprocess.call(['osascript', '-e', 'tell application "Terminal" to do script "{}"'.format(cmd)])

def wifi_info(address):
    cmd = 'networksetup -getinfo Wi-Fi '
    subprocess.call(['osascript', '-e', 'tell application "Terminal" to do script "{}"'.format(cmd)])
    
def show_devices(address):
    try:
        ssid = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]).decode("utf-8").split(" SSID: ")[1].split("\n")[0]
        print(f"Actually wi-fi networK: {ssid}")
    except Exception as e:
        print(f"No info about actually wi-fi: {e}")

    try:
        host_name = os.uname().nodename
        ip_address = subprocess.check_output(["ipconfig", "getifaddr", "en0"]).decode("utf-8").strip()
        print(f"Actually ip adress: {ip_address}")

        connected_devices = subprocess.check_output(["arp", "-a"]).decode("utf-8")
        print(f"Connected devices:\n{connected_devices}")

    except Exception as e:
        print(f"Cannot find information about connected devices: {e}")

