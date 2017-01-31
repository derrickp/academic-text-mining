""" actemin package is used to read text from PDFs and then send that through spaCy
"""

from pdflooper import get_pdf_filenames, write_text_file

def main():
    """ main function for actemin
    """
    file_names = get_pdf_filenames(".\\data")

    out_path = ".\\out_txt"
    for file_name in file_names:
        success = write_text_file(file_name, out_path)
        print(file_name + " " + str(success))

if __name__ == "__main__":
    main()
