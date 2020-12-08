import socket
import tkinter as tk
import psutil as ps
from getpass import getuser
from platform import uname
from time import time
from datetime import datetime
from subprocess import Popen

def get_size(bytesize, suffix="B"):
    #Scale bytes to its proper format
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytesize < factor:
            return f"{bytesize:.2f}{unit}{suffix}"
        bytesize /= factor

win = tk.Tk()
win.geometry('725x600')
win.configure(bg='#0f0f0f')
win.title('System info')
win.iconbitmap('pc.ico')

tk.Label(win, text = 'System Info\n', fg = 'white', bg='#0f0f0f').pack()

start = time()
raminfo = ps.virtual_memory()
tk.Label(win, text = f'Available RAM: {get_size(raminfo.available)}', fg = 'white', bg='#0f0f0f').pack()

bt_timestamp = ps.boot_time()
bt = datetime.fromtimestamp(bt_timestamp)
tk.Label(win, text = f'Computer boot time: {bt.year}/{bt.month}/{bt.day} at {bt.hour}:{bt.minute}', fg = 'white', bg='#0f0f0f').pack()

del bt_timestamp
del bt

tk.Label(win, text = f'Computer hostname: {socket.gethostname()}', fg = 'white', bg='#0f0f0f').pack()
tk.Label(win, text = f'CPU cores: {ps.cpu_count(logical=False)}', fg = 'white', bg='#0f0f0f').pack()
tk.Label(win, text = f'CPU information: {uname().processor}', fg = 'white', bg='#0f0f0f').pack()
tk.Label(win, text = f'CPU logical processors: {ps.cpu_count(logical=True)}', fg = 'white', bg='#0f0f0f').pack()
tk.Label(win, text = f'Currently logged on user: {getuser()}', fg='white', bg='#0f0f0f').pack()
tk.Label(win, text = f'IPv4 address: {socket.gethostbyname(socket.gethostname())}', fg = 'white', bg='#0f0f0f').pack()
tk.Label(win, text = f'OS: {uname().system}', fg = 'white', bg='#0f0f0f').pack()
tk.Label(win, text = f'OS version: {uname().version}', fg = 'white', bg='#0f0f0f').pack()
tk.Label(win, text = f'Total RAM: {get_size(raminfo.total)}', fg = 'white', bg='#0f0f0f').pack()
tk.Label(win, text = f'Used RAM: {get_size(raminfo.used)}\n', fg='white', bg='#0f0f0f').pack()
end = time()

del raminfo

tk.Label(win, text = f'\nRetrieved system info in {end - start} sec\n', fg = 'white', bg='#0f0f0f').pack()

del start, end

def openSourceCode():
    Popen(["notepad.exe", __file__])

tk.Button(win, text = 'Open source code', command=openSourceCode).pack()
del openSourceCode

win.mainloop()
