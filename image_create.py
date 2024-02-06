import fitz
from unidecode import unidecode
from PIL import Image , ImageDraw,ImageFont 
from ftlangdetect import detect
#iso lang code hi sa en 

def create_image(text_data,box_no):
      image = Image.new("RGB", (1500, 1500), "white")
      draw=ImageDraw.Draw(image)
      font_path='/Users/adithyalbhat/github/IITB/Sanskrit_Italic.TTF'
      font = ImageFont.truetype(font_path, size=40)
      draw.text((30,750),text_data,font=font,fill="black",align="right")
      image_path = f"images/{box_no}.jpg"
      image.save(image_path)

box_no=0
doc=fitz.open("Sanskrit_Text.pdf")
bounding_boxes={}
new_list=list()
for page_num in range(doc.page_count):
    page=doc[page_num]
    a=page.get_text().split("\n")
    # print(a)

    for i in a :
        result = detect(text=i, low_memory=False)
        if result['lang']=='sa':
             print(i)
             create_image(unidecode(i),f"box_no{box_no + 1}")
             box_no+=1