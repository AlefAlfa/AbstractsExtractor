import requests
from bs4 import BeautifulSoup
import os

def get_url(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Try extracting URL from the <script> tag
    script_tag = soup.find('script')
    if script_tag:
        # Split the script content by single quotes and extract the URL
        parts = script_tag.string.split("'")
        if len(parts) > 1:
            return parts[1]
    
    # If not found in the <script> tag, try the <noscript> tag
    meta_tag = soup.find('meta', {'http-equiv': 'refresh'})
    if meta_tag:
        content = meta_tag.get('content', '')
        parts = content.split('url=')
        if len(parts) > 1:
            print(parts[1])
            return parts[1]
        

    return None



def get_html(url):
    with requests.get(url, stream=True) as response:
        # Check if the request was successful
        response.raise_for_status()
        print(response.text)
        

        # Check if the content type is html (Optional but recommended)
        if 'text/html' not in response.headers.get('content-type', ''):
            print("The URL does not point to valid html.")
            return

        return response.text
        

def get_pdfs(urls, save_path):
    for idx, url in enumerate(urls):
        html_content = get_html(url)
        pdf_url = get_url(html_content)
        with requests.get(pdf_url, stream=True) as response:
            try:
                # Check if the request was successful
                response.raise_for_status()

                # Check if the content type is PDF
                if 'application/pdf' not in response.headers.get('content-type', ''):
                    print(f"The URL {pdf_url} does not point to a valid PDF.")
                    continue

                # Write content in chunks to handle large files
                filename = f"file{idx}.pdf"
                save_path = os.path.join(save_path, filename)
                with open(save_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192): 
                        file.write(chunk)
                print(f"Downloaded PDF to {save_path}")

            except requests.RequestException as e:
                print(f"Error downloading from URL {pdf_url}: {e}")
                continue


if __name__ == "__main__":    
    url = "https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2310.10467&hl=en&sa=X&d=10337634914763066369&ei=Zkc6ZZnNGI-8ywTFg6egBg&scisig=AFWwaeb_mAYabVFhRFsJEnl5WZxE&oi=scholaralrt&hist=ddnWGi4AAAAJ:6957128465323877680:AFWwaeaTwKVXwlhpuyDdYXZYCzLp&html=&pos=0&folt=kw-top"
    get_pdfs(url, "./pdfs/file.pdf")