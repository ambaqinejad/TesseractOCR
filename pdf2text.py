import os
import fitz

for root, dirs, files in os.walk(r"C:\Users\Chromium\Desktop\law"):
    for dir in dirs:
        sub_dir = os.path.join(root, dir)
        for r, d, f in os.walk(sub_dir):
            for file_name in f:
                file_path = os.path.join(sub_dir, file_name)
                if file_path.lower().endswith(".pdf"):
                    try:
                        doc = fitz.open(file_path)
                        full_text = ""
                        for page in doc:
                            full_text += page.get_text()
                        with open(file_path.split(".")[0] + "-2.txt", "a", encoding="utf8") as converted:
                            print(converted)
                            converted.write(full_text)
                    except Exception as e:
                        print(":(")