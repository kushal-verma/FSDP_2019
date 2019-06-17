
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

presented = input("presented to")
authorised = input("from date")
img = Image.open("C:\\Users\\kushal\\Desktop\\FSDP2019\\Day10\\gift-certificate.jpg.jpg")

draw = ImageDraw.Draw(img)
selectFont = ImageFont.truetype("arial.ttf", size = 60)
draw.text( (200,170), presented, (255,0,0), font=selectFont)
draw.text( (200,192), authorised, (255,0,0), font=selectFont)
img.save( 'certi.pdf', "PDF", resolution=100.0)
          
          