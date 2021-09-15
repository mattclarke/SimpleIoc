# Simple script to read  the waveform and aai records
from epics import PV

PV_ROOT = "SIMPLE:"

def read_record(name, as_str=False):
    p = PV(name)
    print(name, " = ", p.get(as_string=as_str))


read_record(f"{PV_ROOT}WAVE")
read_record(f"{PV_ROOT}CHARWAVE", True)
read_record(f"{PV_ROOT}AAI")

