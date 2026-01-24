from pdf2image import convert_from_path

files = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf', 'file5.pdf']  

for filename in files:
    try:
        pages = convert_from_path(filename)

        for i, page in enumerate(pages):
            output_filename = f'{filename[:-4]}.jpg'  
            page.save(output_filename, 'JPEG')
            
    except Exception as e:
        print(f"ошибка '{filename}': {e}")