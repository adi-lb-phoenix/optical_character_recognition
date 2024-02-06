#import langid
#langid.set_languages(["hi","sa","en"])
import json
from ftlangdetect import detect
from unidecode import unidecode
# from inltk.inltk import identify_language, reset_language_identifying_models
result = detect(text="शाϞϵलࣺवΕࣺࣞडतͳ", low_memory=False)
# from inltk.inltk import identify 
# result=detect(text="इ܃वΚा",low_memory=False)
#print(langid.classify("उदाहरणͳ"))
print(result['lang'])

import fitz
from PIL import Image , ImageDraw
from ftlangdetect import detect

def create_image(text_data,box_no):
      image = Image.new("RGB", (200, 200), "white")
      draw=ImageDraw.Draw(image)
      draw.text((50,50),text_data,fill="black",align="right")
      image_path = f"images/{box_no}.jpg"
      image.save(image_path)

def write_json(data,filename="annot_data.json"):
      with open(filename,'r+') as file:
            try:
                file_data=json.load(file)
            except json.decoder.JSONDecodeError:
                  file_data={}
            print("data_length and type",len(data),type(data))
            # key,value=data.popitem()
            # file_data[key]=value
            #file.seek(0)
            file_data.update(data)
            file.seek(0)
            json.dump(file_data,file,indent=4)
            file.truncate() 

            
box_no=0
#iso lang code hi sa en 
doc=fitz.open("Sanskrit_Text.pdf")
bounding_boxes={}
i='राߺोयϳयोࣆवϳयोगोऽࠋौ त׽ृ ؖो߱39 चतुःशती '
for page_num in range(doc.page_count):
    page=doc[page_num]
    text_instances=page.search_for(unidecode(i))
    print("this is text instances",text_instances)
    for text_instance in text_instances:
            #print("this is the length of text_instance within text_instances",len(text_instance))
            print(text_instance)
            x0,y0,x1,y1=text_instance
            print(x0,y0,x1,y1)
            # top_left=[x0,y]
            print("\n")

            bounding_boxes={

    f"box_no{box_no+1}": {

"top_left": [x0,y0],

"top_right": [x1,y0],

"bottom_left": [x0, y1],

"bottom_right": [x1,y1]

            }

            }
            box_no=box_no+1
            write_json(bounding_boxes)
            print(bounding_boxes)
            create_image(i,f"box_no{box_no+1}")



            