import subprocess

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

