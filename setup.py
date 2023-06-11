#!/usr/bin/env python3

import subprocess, sys

if __name__ == "__main__":
    subprocess.call ("mkdir -p ~/pdk", shell=True)
    subprocess.call ("mv ./lib/ ~/pdk", shell=True)
    subprocess.call ("mv ./verilog/ ~/pdk", shell=True)
    subprocess.call ('echo "export PDK_ROOT=~/pdk" >> ~/.bashrc', shell=True)
    subprocess.call ("source ~/.bashrc", shell=True)