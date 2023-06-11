#!/usr/bin/env python3

import subprocess, sys

if __name__ == "__main__":
    subprocess.call ("mkdir -p ~/material", shell=True)
    subprocess.call ("mv ./pdk/ ~/material", shell=True)
    subprocess.call ("mv Makefile ~/material", shell=True)
    subprocess.call ('echo "export PDK_ROOT=~/material/pdk" >> ~/.bashrc', shell=True)
    subprocess.call ("source .zshrc", shell=True)