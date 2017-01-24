academic-text-mining (actemin)
===

## Description

- A Python package whose goal is to be able to take the text from academic papers and retrieve information from it.  
- The academic papers used for this were geographic papers. The key piece of information intended to be retrieved from the papers is where the study took place, and the time of the study.

## Dependencies

- [spaCy](https://spacy.io/)
- [pdfrw](https://github.com/pmaupin/pdfrw)
    - pdfrw is a library for reading and writing pdf files.  
      In this package it will be used to read the text from the pdf files in the configured directories. This text will then be sent through spaCy to eventually pull out information.