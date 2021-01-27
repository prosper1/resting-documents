import PyPDF2
from PyPDF2 import pdf
from PyPDF2.generic import decode_pdfdocencoding


def pdf_to_text(file,password):
    pdf_file = open(file, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # If encrypted, decrypt it with the password
    if pdf_reader.isEncrypted:  
        pdf_reader.decrypt(password) 
    

    # map PDF page content by page_number
    result = map(
        lambda page:  pdf_reader.getPage(
            list(pdf_reader.pages).index(page)).extractText(),
        list(pdf_reader.pages)
        )

    return list(result)

    