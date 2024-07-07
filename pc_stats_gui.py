from PIL import Image
Image.CUBIC = Image.BICUBIC
from tkinter import *
import ttkbootstrap as ttb
from ttkbootstrap.tooltip import ToolTip
import os, psutil, platform, cpuinfo
import time


storage = {}

def get_storage_info():
    disk_count = 0
    for ad in psutil.disk_partitions():
        disk_info = psutil.disk_usage(path=ad[disk_count])
        storage['Drive' + ad[disk_count]] = dict(
            {
                'total_disk_space': str(round(disk_info[0] / 1024 ** 3, 1)) + 'GB',
                'used_disk_space': str(round(disk_info[1] / 1024 ** 3, 1)) + 'GB',
                'used_disk_percent': str(disk_info[3]) +'%',
            }
        )
        disk_count += 1
    return storage


class Dashboard(ttb.Frame):
    def __init__(self, main):
        super().__init__(main, padding=(20,20))
        self.pack(fill=BOTH, expand=YES)
        self.board = platform.node()
        self.cpu = cpuinfo.get_cpu_info()['brand_raw']
        self.num_cores = cpuinfo.get_cpu_info()['count']/2
        self.num_threads = cpuinfo.get_cpu_info()['count']
        self.proc_speed = cpuinfo.get_cpu_info()['hz_actual_friendly']
        self.total_ram = psutil.virtual_memory().total/1024**3
        self.available_disks = [d[0] for d in psutil.disk_partitions()]
        self.cpu_usage = psutil.cpu_percent()
        self.ram_usage = psutil.virtual_memory().percent

        self.create_label(self.board)
        self.create_label(self.cpu)
        self.create_label(self.total_ram)
        self.create_label(f'{len(self.available_disks)} available disks')
        #self.create_label(self.proc_speed)

        self.create_meter("CPU Usage", self.cpu_usage)
        self.create_meter("RAM Usage", self.ram_usage)

    def create_label(self, label):
        lab = ttb.Label(self, text=label)
        lab.pack()

    def create_meter(self, label, variable):
        meter = ttb.Meter(self, metersize=150, padding = 10, amounttotal=100, metertype="semi", interactive=False, subtext=label, textright="%")
        meter.pack()
        meter.configure(amountused=variable)

    def update(self):
        return
    
if __name__ == "__main__":
    app = ttb.Window("Dashboard", "darkly")
    Dashboard(app)
    app.mainloop()