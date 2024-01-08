import tkinter as tk


from GUI_BUTTONS_WINDOWS import create_button_ping
from GUI_BUTTONS_WINDOWS import create_button_traceroute
from GUI_BUTTONS_WINDOWS import create_button_curl
from GUI_BUTTONS_WINDOWS import create_info_wifi_button

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Commands with terminal")
    root.configure(background='lightgreen')

    create_button_ping(root)
    create_button_traceroute(root)
    create_button_curl(root)
    create_info_wifi_button(root)

    root.mainloop()
