# certificate generation based on given xl data
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_excel (r'sat.xlsx') 
name_list = data["Name"].tolist() 
for i in name_list:
    im = Image.open(r'g.jpg')
    date="21-02-2021 to 27-02-2021"
    prog="Python Basics"
    d = ImageDraw.Draw(im)
    location = (295, 159)
    location1=(305, 193)
    location2=(305,335)
    text_color = (1, 137, 209)#color options
    font = ImageFont.truetype("arial.ttf", 20)
    font2 = ImageFont.truetype("arial.ttf", 15)
    d.text(location, i, fill = text_color, font = font)
    d.text(location1,prog,fill=text_color,font=font2)
    d.text(location2,date,fill=text_color,font=font)
    im.save("certificate_of" + i + ".png")



#**** Done by satheesh**
