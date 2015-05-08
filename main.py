#!/usr/bin/env python

import sys
import pyautogui
import pyqrcode


def generate_qr_code():
    with open("sl4a/QR-IO.py", "r") as src:
        data = src.readlines()

    code = pyqrcode.create('www.loopback-lan.se')
    print(code.terminal(module_color='red', background='yellow'))
    # url.svg('QR-IO-Android-source.svg', scale=4)
    # code.png('QR-IO-Android-source.png', scale=6)


def send_keys():
    pyautogui.typewrite('Hello world!')

generate_qr_code()
