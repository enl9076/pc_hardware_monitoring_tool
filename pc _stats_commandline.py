import os, psutil, platform, cpuinfo
import pprint
import time
import tabulate


available_disks = [d[0] for d in psutil.disk_partitions()]
board = platform.node()
cpu = cpuinfo.get_cpu_info()['brand_raw']
num_cores = cpuinfo.get_cpu_info()['count']/2
num_threads = cpuinfo.get_cpu_info()['count']
proc_speed = num_cores = cpuinfo.get_cpu_info()['hz_actual_friendly']
total_ram = psutil.virtual_memory().total/1024**3
headers=("Motherboard", "Processor", "Cores", "Threads", "Processing Speed", "Total RAM")
pc_info = [board, cpu, str(num_cores), str(num_threads), proc_speed, str(round(total_ram, 2))]
static_info = dict(zip(headers, pc_info))

statistics = {}

def get_storage_info():
    disk_count = 0
    for ad in psutil.disk_partitions():
        disk_info = psutil.disk_usage(path=ad[disk_count])
        statistics['Drive' + ad[disk_count]] = dict(
            {
                'total_disk_space': str(round(disk_info[0] / 1024 ** 3, 1)) + 'GB',
                'used_disk_space': str(round(disk_info[1] / 1024 ** 3, 1)) + 'GB',
                'used_disk_percent': str(disk_info[3]) +'%',
            }
        )
        disk_count += 1
    return statistics


def update_metrics():

    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    statistics['cpu_usage'] = cpu_usage
    statistics['ram_usage'] = ram_usage
    get_storage_info()
    return statistics

pprint.pprint(static_info)
pprint.pprint(get_storage_info())
while True:
    tabulate.tabulate(update_metrics())
    pprint.pprint(update_metrics())
    time.sleep(2)


