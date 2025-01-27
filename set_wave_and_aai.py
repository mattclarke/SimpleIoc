# Simple script to write random values to the waveform and aai records
import random
from p4p.client.thread import Context

_CONTEXT = Context('pva', nt=False)
PV_ROOT = "SIMPLE:"


def generate_data():
    data = [1, 5, 10, 3, 0]
    random.shuffle(data)
    return data


def generate_char_data():
    data = [chr(97), chr(98), chr(99), chr(100), chr(101)]
    random.shuffle(data)
    return "".join(data)


def generate_str_data():
    data = ["hello", "goodbye", "ciao", "hej", "shrug"]
    random.shuffle(data)
    return data


def update_record(name, data, as_str=False):
    print(name)
    _CONTEXT.put(name, data, wait=True)
    print(_CONTEXT.get(name).value)


update_record(f"{PV_ROOT}WAVE", [x for x in range(500)])
update_record(f"{PV_ROOT}CHARWAVE", generate_char_data(), True)
update_record(f"{PV_ROOT}STRWAVE", generate_str_data(), True)
update_record(f"{PV_ROOT}AAI", generate_data())

