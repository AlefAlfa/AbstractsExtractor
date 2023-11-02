from get_emails import get_links_from_email
from get_pdfs import get_pdfs
from extract import extract

links = get_links_from_email()

get_pdfs(links, ".")
    