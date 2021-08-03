import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/"

url = pyqrcode.create(s)

url.svg("myyoutube.svg", scale = 8)