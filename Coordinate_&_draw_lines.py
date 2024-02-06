import fitz
from unidecode import unidecode
from PIL import Image , ImageDraw
from ftlangdetect import detect
from test_lang import write_json
import json 
import langid 
#iso lang code hi sa en 

def draw_rect(page,rect_coordinates):
    page.draw_rect(rect_coordinates,color=(1,0,0),width=2)

doc=fitz.open("Sanskrit_Text.pdf")
bounding_boxes={}

box_no=1
for page_num in range(doc.page_count):
    page=doc[page_num]
    a=page.get_text("blocks")
    # print(a)

    for i in a :
        print(i[4].split("\n")[:])
        lines=i[4].split("\n")[:]
        for stnc in lines:
            result = detect(text= stnc, low_memory=False)
            if result['lang']=='sa':
                print(stnc,result['lang'],f"box_no_{box_no}","\n")
                print(i[:4],"\n\n\n")
                x0=i[0]
                y0=i[1]
                x1=i[2]
                y1=i[3]
                bounding_boxes={

            f"box_no_{box_no}": {

            "top_left": [x0,y0],

            "top_right": [x1,y0],

            "bottom_left": [x0, y1],

            "bottom_right": [x1,y1]

            }

            }
                write_json(bounding_boxes)
                box_no+=1

                draw_rect(page,(x0, y0, x1, y1))
                # text_instances=page.search_for(i)
                # # print(text_instances)
                # for text_instance in text_instances:
                #     x0,y0,x1,y1=text_instance.bbox 

                # print(f"Bounding Box: ({x0}, {y0}) - ({x1}, {y1})")
        # print(i,result['lang'])
        

    print("\n\n\n")
    

output_pdf_path = "output_with_rectangles.pdf"
doc.save(output_pdf_path)
doc.close()
    
    
       # Iterate through each instance and print the bounding box coordinates
   
   
    

# def extract_text_and_create_boxes(pdf_path):
#     doc=fitz.open("Sanskrit_Text.pdf")

#     for page in doc:
#         text_instances=page.search_for(search_text)

#     bounding_box={}

    #for page_num in range(doc.page_count):