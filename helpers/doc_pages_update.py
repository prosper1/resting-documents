import documents
from documents.models import Document, TextPages
from .pdf import pdf_to_text
from helpers import pdf


def save():
    documents = Document.objects.filter(has_page=False)

    for document in documents:
        page_count =0
        pages = pdf_to_text(document.file.path,"")

        for page in pages:
            page = TextPages.objects.create(
                document = document,
                page_number = page_count,
                content = page
                )
            page_count = page_count + 1
            page.save()

        


