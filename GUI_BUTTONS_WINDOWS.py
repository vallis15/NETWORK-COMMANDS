import tkinter as tk
from Tests import ping_test
from Tests import traceroute_test
from Tests import show_curl
from Tests import wifi_info
from Tests import show_devices
from Tests import speed_test

def create_button_ping(root):

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10)
    entry = tk.Entry(frame, width=20)
    entry.pack(side="left", padx=(0, 10))
    button = tk.Button(frame, text="Ping", command=lambda: click_ping(entry))
    button.pack(side="left")

def click_ping(entry):
    address = entry.get()
    ping_test(address)

def create_button_traceroute(root):
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10)
    entry = tk.Entry(frame, width=20)
    entry.pack(side="left", padx=(0, 10))
    button = tk.Button(frame, text="Traceroute", command=lambda: click_traceroute(entry))
    button.pack(side="left")

def click_traceroute(entry):
    address = entry.get()
    traceroute_test(address)

def create_button_curl(root):
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10)
    entry = tk.Entry(frame, width=20)
    entry.pack(side="left", padx=(0, 10))
    button = tk.Button(frame, text="CURL", command=lambda: click_CURL(entry))
    button.pack(side="left")

def click_CURL(entry):
    address = entry.get()
    show_curl(address)

def create_info_wifi_button(root):
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10)
    button = tk.Button(frame, text="Info about your Wi-Fi", command=lambda: wifi_info("Wi-Fi"))
    button.pack(side="left")
    
def create_devices_button(root):
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10)
    button = tk.Button(frame, text="Show devices connected on your wi-fi", command=lambda: show_devices("Wi-fi"))
    button.pack(side="left")
    
def create_speed_button(root):
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10)
    button = tk.Button(frame, text="Test your connection speed", command=speed_test)
    button.pack(side="left")
    
    







