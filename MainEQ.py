import pyaudio
import numpy as np
import pylab
import time

RATE = 192000
CHUNK = int(RATE / 20)  # RATE / number of updates per second

pyAudio = pyaudio.PyAudio()
info = pyAudio.get_host_api_info_by_index(0)
for i in range(0, info.get('deviceCount')):
    if (pyAudio.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", pyAudio.get_device_info_by_host_api_device_index(0, i).get('name'))

stream = pyAudio.open(format=pyaudio.paInt24, channels=2, rate=RATE, input=True, input_device_index=1, frames_per_buffer=CHUNK)
