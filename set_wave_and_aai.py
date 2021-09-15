# Simple script to write random values to the waveform and aai records
from epics import PV
import random

PV_ROOT = "SIMPLE:"

def generate_data():
    return [random.randint(0, 20) for _ in range(5)]


def generate_char_data():
    return "".join([chr(97 + random.randint(0, 25)) for _ in range(5)])


def update_record(name, data):
    print(name)
    p = PV(name)
    p.put(data, wait=True)
    print(p.get())


print(generate_data())
update_record(f"{PV_ROOT}WAVE", generate_data())
update_record(f"{PV_ROOT}CHARWAVE", generate_char_data())
update_record(f"{PV_ROOT}AAI", generate_data())

