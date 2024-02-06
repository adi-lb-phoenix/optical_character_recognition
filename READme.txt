problem statement :
you have to create bounding
boxes for each line in the Sanskrit text that is provided in the attached
file. After the bounding box is created for the entire line (and not the
words). You need
to save each line in separate jpg files and send us the output.


Additionally, you need to save the coordinates of the bounding box in a JSON
format as shown below:


{

"box1": {

"top_left": [0, 0],

"top_right": [0, 10],

"bottom_left": [10, 0],

"bottom_right": [10, 10]

},

"box2": {

       ....

}

}










"output_with_rectangles.pdf" contains the pdf with rectangluar boxes around sanskrit texts 

Sanskrit_italic.TTF is the devanagiri font used while printing the sanskrit text in the image .

Coordinate_&_draw_lines contains script for finding out coordinates and draw the bounding boxes for sanskrit text.

write_to_json.py contains the function used to write the json file that is annot_data.json

images folder contains all the sanskrit texts in an jpg format 



pip list 
Package             Version
------------------- ----------
annotated-types     0.6.0
blis                0.7.11
catalogue           2.0.10
certifi             2023.11.17
cffi                1.16.0
charset-normalizer  3.3.2
click               8.1.7
cloudpathlib        0.16.0
confection          0.1.4
contourpy           1.2.0
cycler              0.12.1
cymem               2.0.8
fasttext            0.9.2
fasttext-langdetect 1.0.5
filelock            3.13.1
fonttools           4.47.2
frozenlist          1.4.1
fsspec              2023.12.2
idna                3.6
importlib-resources 6.1.1
Jinja2              3.1.3
kiwisolver          1.4.5
langcodes           3.3.0
langid              1.1.6
MarkupSafe          2.1.4
mpmath              1.3.0
multidict           6.0.4
murmurhash          1.0.10
networkx            3.2.1
numpy               1.26.3
packaging           23.2
pillow              10.2.0
pip                 23.3.2
preshed             3.0.9
pybind11            2.11.1
pycparser           2.21
pydantic            2.6.0
pydantic_core       2.16.1
PyMuPDF             1.23.20
PyMuPDFb            1.23.9
pyparsing           3.1.1
python-dateutil     2.8.2
pytz                2023.4
pyvips              2.2.2
PyYAML              6.0.1
requests            2.31.0
scipy               1.12.0
setuptools          58.0.4
six                 1.16.0
smart-open          6.4.0
soupsieve           2.5
spacy               3.7.2
spacy-legacy        3.0.12
spacy-loggers       1.0.5
srsly               2.4.8
sympy               1.12
thinc               8.2.2
torch               2.2.0
torchvision         0.17.0
tqdm                4.66.1
typer               0.9.0
typing_extensions   4.9.0
tzdata              2023.4
unicode             2.9
Unidecode           1.3.8
urllib3             2.2.0
wasabi              1.1.2
weasel              0.3.4
yarl                1.9.4
zipp                3.17.0

these were all the packages i did install at the time , a lot of them were not used .