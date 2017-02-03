academic-text-mining (actemin)
===

## Description

- A Python package whose goal is to be able to take the text from academic papers and retrieve information from it.  
- The academic papers used for this were geographic papers. The key piece of information intended to be retrieved from the papers is where the study took place, and the time of the study.

## Configuration
- Configuration for the application is stored in YAML format. By default the application looks for configurations in `actemin/config/config.yml`

## Dependencies

- Python 2.7 - Using Python 2.7 because of rasa. rasa requires Python 2.7 (3 is in the roadmap)
- [spaCy](https://spacy.io/)
- [tika](https://github.com/chrismattmann/tika-python)
  - As part of this you will also need tika server
  - [tika-server](https://wiki.apache.org/tika/TikaJAXRS)
  - Start the tika server and then you can run the pdf parsing portion of the application