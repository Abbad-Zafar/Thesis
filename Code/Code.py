# importing required modules
from PyPDF2 import PdfReader
import camelot

import json

filename = 'BMW-2021.pdf'

x = filename.split(".pdf")
report_name = x[0]
y = report_name.split("-")
report_company_name=y[0]
report_year=y[1]

# creating a pdf reader object
reader = PdfReader(filename)

info = reader.metadata
print(info)

# printing number of pages in pdf file
print(len(reader.pages))
page_number = 9
# getting a specific page from the pdf file
page = reader.pages[page_number - 1]

# extracting text from page
text = page.extract_text()

text_block = {
    "id": 1,
    "page_number": page_number,
    "text": text,
    "total_pages": len(reader.pages),
    "filename": filename,
    "report_name": report_name,
    "report_company_name": report_company_name,
    "report_year": report_year
    }


# Serializing json  
json_object = json.dumps(text_block) 
print(json_object)

# PDF file to extract tables from
# file = "BMW-2021.pdf"
# tables = camelot.read_pdf(file)
# print("Total tables extracted:", tables.n)
# print(tables[0].df)



# import tabula
# pdf_path = "BMW-2021.pdf"
# dfs = tabula.read_pdf(pdf_path, pages='9')
# print(len(dfs))
# print(dfs[0])


# import tika
# from tika import parser

# FileName = "BMW-2021.pdf"
# PDF_Parse = parser.from_file(FileName)
# print(PDF_Parse ['content'])
# print(PDF_Parse ['metadata']) # Format-Dictionary

import fitz # PyMuPDF
import io
from PIL import Image

# file path you want to extract images from
file = "BMW-2021.pdf"
# open the file
pdf_file = fitz.open(file)

# iterate over PDF pages
for page_index in range(len(pdf_file)):
    # get the page itself
    page = pdf_file[page_index]
    image_list = page.get_images()
    # printing number of images found in this page
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.get_images(), start=1):
        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        # get the image extension
        image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
        image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))


