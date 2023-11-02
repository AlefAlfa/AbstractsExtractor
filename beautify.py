from bs4 import BeautifulSoup
import quopri

def get_links(html):
    decoded_html = quopri.decodestring(html).decode('utf-8')
    soup = BeautifulSoup(decoded_html, 'html.parser')

    # Extracting the titles and links
    links = []
    for a_tag in soup.find_all('a', class_='gse_alrt_title'):
        link = a_tag['href']
        links.append(link)

    # Printing the extracted data
    return links
