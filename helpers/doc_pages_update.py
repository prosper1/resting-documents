import documents
from documents.models import Document, TextPages
from .pdf import pdf_to_text
from helpers import pdf


def save():
    documents = Document.objects.filter(has_page=False)
    
    for document in documents:
        pages = pdf_to_text(document.file,"")
        map(lambda page: TextPages.objects.create(
            document = document,
            page_number = pages.find(page),
            content = page
        ),pages)


