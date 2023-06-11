#!/usr/bin/env python3

import subprocess

if __name__ == "__main__":
    subprocess.call ("mkdir -p ~/sky130A", shell=True)
    subprocess.call ("mv ./lib/ ~/sky130A", shell=True)
    subprocess.call ("mv ./verilog/ ~/sky130A", shell=True)
    subprocess.call ('echo "export PDK_ROOT=~/sky130A" >> ~/.bashrc', shell=True)
    subprocess.call ('echo "source ~/.bashrc" >> ~/.bash_profile', shell=True)