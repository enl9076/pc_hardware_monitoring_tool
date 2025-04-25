import os, re, shutil, psutil
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
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

statistics=update_metrics()

st.set_page_config(page_title="Sensor Panel", page_icon="", layout="wide")
st.text(board)
st.text(cpu)
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 270,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "CPU Usage"}))

col1, col2, col3 = st.columns(3)
placeholder = st.empty()
while True:
    statistics=update_metrics()
    with placeholder.container():
        col1.metric(
        label="CPU Usage",
        value=round(statistics['cpu_usage'],2),
    )

        col2.metric(
        label="Disk Space",
        value=statistics['total_disk_space'],
    )

        col3.metric(
        label="Free Disk Space",
        value=statistics['free_disk_space'],
    )
    time.sleep(5)