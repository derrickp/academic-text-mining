""" Code to get text from all pdfs in a directory
Function to return a list of pdf file names
Function that takes in a pdf file path, and an out path,
and writes the contents of the pdf to disk at location. If it can be parsed correctly.
"""

from os import walk, path
from tika import parser
import codecs

def get_pdf_filenames(folder_path):
    """ Returns array of pdf file names that are in specified path """
    pdf_file_names = []
    for subdir, dirs, files in walk(folder_path):
        for file_name in files:
            if file_name.endswith(".pdf"):
                full_path = path.join(subdir, file_name)
                pdf_file_names.append(full_path)
    return pdf_file_names


def write_text_file(pdf_file_path, out_path, server_endpoint="http://localhost:9998"):
    """ Write contents of pdf file to a text file """
    text_file_name = path.splitext(path.basename(pdf_file_path))[0] + ".txt"
    text_file_path = path.join(out_path, text_file_name)
    parsed = parser.from_file(pdf_file_path, server_endpoint)
    success = False

    if parsed["content"] != None:
        success = True
        with codecs.open(text_file_path, "w", encoding='utf-8') as text_file:
            text_file.write(pdf_file_path)
            write_dictionary_to_file(text_file, parsed["metadata"])
            write_content_to_file(text_file, parsed["content"])
    return success


def write_dictionary_to_file(text_file, metadata):
    """ Writes the given dictionary to the given file.
        Only checks to see if the value in the dictionary is a list or None
        otherwise just writes to file
    """
    for key, val in metadata.items():
        if isinstance(val, list):
            text_file.write(key + ": \n")
            for line in val:
                if line != None:
                    text_file.write(line + "\n")
        else:
            text_file.write(key + ": " + val + "\n")


def write_content_to_file(text_file, content):
    """ Writes the given content to the text file
        First writes a Content tag into the file
    """
    text_file.write("!PDF_CONTENT!\n")
    text_file.write("--------------------------------\n")
    text_file.write(content)
