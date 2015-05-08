#!/usr/bin/env python

import sys
import pyautogui
import pyqrcode


def generate_qr_code():
    url = pyqrcode.create('http://www.computerhope.com/issues/ch000178.htm')
    url.svg(sys.stdout, scale=1)
    url.svg('uca.svg', scale=4)


def send_keys():
    pyautogui.typewrite('Hello world!')

generate_qr_code()
