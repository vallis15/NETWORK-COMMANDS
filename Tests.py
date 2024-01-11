import subprocess
import os
import tkinter as tk
from tkinter import messagebox


def ping_test(address):
    try:
        result = subprocess.run(['ping', '-c', '4', address], stdout=subprocess.PIPE, text=True)
        
        print(result.stdout)
        
        tk.messagebox.showinfo("Ping Result", result.stdout)
    except Exception as e:
        print(f"Ping test doesnt work now: {e}")

def traceroute_test(address):
    try:
        result = subprocess.run(['traceroute', address], stdout=subprocess.PIPE, text=True)
        print(result.stdout)
        messagebox.showinfo("Traceroute Result", result.stdout)
    except Exception as e:
        print(f"Traceroute test doesnt work: {e}")

def show_curl(address):
    try:
        result = subprocess.run(['curl', address], stdout=subprocess.PIPE, text=True)
        print(result.stdout)
        messagebox.showinfo("CURL Result", result.stdout)
    except Exception as e:
        print(f"Show CURL doesnt work now: {e}")

def wifi_info(address):
    try:
        result = subprocess.run(['networksetup', '-getinfo', 'Wi-Fi'], stdout=subprocess.PIPE, text=True)
        print(result.stdout)
        messagebox.showinfo("Wi-Fi Info", result.stdout)
    except Exception as e:
        print(f"Information about your wi-fi doesnt work: {e}")
    
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
        
def speed_test():
    try:
        result = subprocess.run(['speedtest', '--simple'], stdout=subprocess.PIPE, text=True)
        
        print(result.stdout)
        
        tk.messagebox.showinfo("Speed Test Result", result.stdout)
    except Exception as e:
        print(f"Speed test doesn't work now: {e}")

