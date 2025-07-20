from pdf2image import convert_from_path
import os
import pytesseract

for root, dirs, files in os.walk(r"C:\Users\Chromium\Desktop\law"):
    for dir in dirs:
        sub_dir = os.path.join(root, dir)
        for r, d, f in os.walk(sub_dir):
            for file_name in f:
                file_path = os.path.join(sub_dir, file_name)
                if file_path.lower().endswith(".pdf"):
                    text = ""
                    images = convert_from_path(file_path, poppler_path=r"C:\poppler\poppler-24.08.0\Library\bin")
                    for img in images:
                        text += pytesseract.image_to_string(img, lang='fas') + "\n"
                    with open(file_path.split(".")[0]+".txt", "a") as ocred:
                        print(ocred)
                        ocred.write(text)

