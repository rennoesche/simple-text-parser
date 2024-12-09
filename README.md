# PDF file parser into database
Simple PDF file parser into database, using pdfminer and sqlite.

## requirement
- pdfminer
- sqlalchemy
- nltk

## demo
- clone repository
- cd simple-text-parser && install requirements
```bash
pip install -r requirements.txt
```
- make sure punkt downloaded, by uncomment nltk.download in core/tokenize
- add pdf file, default: cv.pdf
- run main.py