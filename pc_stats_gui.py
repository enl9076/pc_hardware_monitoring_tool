from tkinter import *
import ttkbootstrap as ttb
import os, psutil, platform, cpuinfo
import pprint
import time

board = platform.node()
cpu = cpuinfo.get_cpu_info()['brand_raw']
num_cores = cpuinfo.get_cpu_info()['count']/2
num_threads = cpuinfo.get_cpu_info()['count']
proc_speed = num_cores = cpuinfo.get_cpu_info()['hz_actual_friendly']
total_ram = psutil.virtual_memory().total/1024**3
available_disks = [d[0] for d in psutil.disk_partitions()]


root = ttb.Window(themename = "darkly")

root.title("Test Dashboard")
#root.iconbitmap()
root.geometry('500x500')

board_label = ttb.Label(root, text=board, font= ("Ariel", 14))
board_label.pack()

cpu_label = ttb.Label(root, text=cpu, font= ("Ariel", 14))
cpu_label.pack()

num_disks_label = ttb.Label(root, text=f"Number of storage devices: " + str(available_disks), font= ("Ariel", 14))
num_disks_label.pack()
root.mainloop()