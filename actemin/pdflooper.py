""" Code to loop through directory
Function to return a list of pdf file names
Function to return a dictionary of pdf file name to the text of pdf
"""

from os import walk, path
import PyPDF2
import slate

def get_pdf_filenames(folder_path):
    """ Returns array of pdf file names that are in specified path """
    pdf_file_names = []
    for subdir, dirs, files in walk(folder_path):
        for file_name in files:
            full_path = path.join(subdir, file_name)
            pdf_file_names.append(full_path)
    return pdf_file_names

def write_text_file(pdf_file_path, out_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        text_file_path = path.join(out_path,
                                   path.splitext(path.basename(pdf_file_path))[0] + ".txt")
        try:
            doc = slate.PDF(pdf_file)
            with open(text_file_path, "w") as text_file:
                for page_num in range(0, len(doc)-1):
                    page = doc[page_num]
                    print("writing page: " + str(page_num) + " of " + pdf_file_path)
                    text_file.write(page)
                # pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                # for page_num in range(0, pdf_reader.numPages-1):
                #     page_object = pdf_reader.getPage(page_num)
                #     text = page_object.extractText()
                #     print("writing page: " + str(page_num) + " of " + pdf_file_path)
                #     text_file.write(text)
            return True
        except Exception as ex:
            print(str(ex))
            return False
    