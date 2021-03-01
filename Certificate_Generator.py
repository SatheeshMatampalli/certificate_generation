# certificate generation based on given xl data
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_excel (r'sat.xlsx') 
name_list = data["Name"].tolist() 
for i in name_list:
    im = Image.open(r'i.png')
    d = ImageDraw.Draw(im)
    location = (325, 258)
    text_color = (5, 137, 209)#optional
    font = ImageFont.truetype("arial.ttf", 40)
    d.text(location, i, fill = text_color, font = font)
    im.save("certificate_of" + i + ".png")



#**** Done by satheesh**
