import os, re, shutil, psutil
import streamlit as st
import plotly.graph_objects as go
import time

board = 'B550M AORUS ELITE AX'
cpu = 'AMD Ryzen 5 5600G'
#matcher = re.compile('\d+')

statistics = {}

def update_metrics():

    cpu_usage = psutil.cpu_percent()
    cpu_threads = os.cpu_count()
    cpu_cores = cpu_threads/2
    statistics['cpu_threads'] = cpu_threads
    statistics['cpu_cores'] = cpu_cores

    statistics['cpu_usage'] = cpu_usage

    total, used, free = shutil.disk_usage("/")

    statistics['disk'] = dict(
        {
            'total_disk_space': round(total / 1024 ** 3, 1),
            'used_disk_space': round(used / 1024 ** 3, 1),
            'free_disk_space': round(free / 1024 ** 3, 1),
        }
    )

    return(statistics)

while True:
    statistics=update_metrics()
    print(statistics)
    time.sleep(5)