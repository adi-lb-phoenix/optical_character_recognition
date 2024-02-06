
import fitz 
from ftlangdetect import detect
from unidecode import unidecode
from PIL import Image  
from PIL import ImageFont  
from PIL import ImageDraw 
import pyvips
def bgoutput( text,filename):  
 
   rendered_text, feedback = pyvips.Image.text(text,   
                         width=300, height=50,   
                         autofit_dpi=True)
   rendered_text.write_to_file(f"images/{filename}") 

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
             bgoutput(i,f"box_no{box_no + 1}")
             box_no+=1