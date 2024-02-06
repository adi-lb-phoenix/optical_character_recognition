import fitz
from unidecode import unidecode
from PIL import Image , ImageDraw,ImageFont 
from ftlangdetect import detect

box_no=0
doc=fitz.open("Sanskrit_Text.pdf")
bounding_boxes={}
new_list=list()
box_no=1
for page_num in range(doc.page_count):
    page=doc[page_num]
    a=page.get_text("blocks")
    # for i in a :
    #     print(i,"\n")

    for i in a :
        print(i[4].split("\n")[:])
        lines=i[4].split("\n")[:]
        for stnc in lines:
            result = detect(text= stnc, low_memory=False)
        #result = detect(text= i[4].split("\n"), low_memory=False)
        
            if result['lang']=='sa':
                print(stnc ,f"{box_no}","\n" )
                print(i[:4],"\n\n\n")
                #create_image(unidecode(i),f"box_no{box_no + 1}")
                box_no+=1