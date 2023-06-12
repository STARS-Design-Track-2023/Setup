#!/usr/bin/env python3

import subprocess, os

if __name__ == "__main__":
    subprocess.call ("mkdir -p ~/sky130A", shell=True)
    subprocess.call ("mv ./lib/ ~/sky130A", shell=True)
    subprocess.call ("mv ./verilog/ ~/sky130A", shell=True)
    subprocess.call ('echo "\nexport PDK_ROOT=~/sky130A" >> ~/.bashrc', shell=True)
