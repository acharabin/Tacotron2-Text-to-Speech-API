import json
import numpy as np
import requests
from IPython.display import Audio

def play_ac_voice(text, samplingrate=22050, maxwavvalue=32768, api="http://159.203.49.85:5000/predict", maxcharacters=200):
    if len(text)>maxcharacters: return print(f"""inputted text length above maximum value of {maxcharacters}""")
    response = requests.post(f"{api}", json={"text":text})
    data=np.array(response.json())
    scaled = np.int32(data / np.max(np.abs(data)) * maxwavvalue)
    return Audio(scaled, rate=samplingrate, autoplay=True)