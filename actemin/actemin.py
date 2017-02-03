""" actemin package is used to read text from PDFs and then send that through spaCy
"""

import sys
import yaml
from pdflooper.utilities import write_text_file, get_pdf_filenames

def read_pdfs(pdf_directory, out_path):
    """ Read the contents of a directory of pdfs to text files
        Text files placed in out_path
    """
    file_names = get_pdf_filenames(pdf_directory)
    print(file_names)
    for file_name in file_names:
        success = write_text_file(file_name, out_path)
        if success:
            print("wrote text file for: " + file_name)
        else:
            print("could not get content of: " + file_name)


def main(config_path):
    """ main function for actemin
    """
    if config_path is None:
        config_path = "./config/config.yml"
    with open(config_path) as config_file:
        config = yaml.load(config_file)

    text_file_directory = config["text_file_directory"]
    if config["read_pdfs"]:
        read_pdfs(config["pdf_directory"], text_file_directory)


if __name__ == "__main__":
    CONFIG_FILE_PATH = sys.argv[1]
    main(CONFIG_FILE_PATH)
