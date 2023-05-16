import pyqrcode
import png 
# from pyqrcode import QRcode

website="https://en.wikipedia.org/wiki/Main_Page"

myQRcode=pyqrcode.create(website)

myQRcode.png("wikipedia.png",scale=6)

print(myQRcode)