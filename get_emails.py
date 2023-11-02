from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow 
from google.auth.transport.requests import Request 
import pickle 
import os.path 
import base64 
import email 
from bs4 import BeautifulSoup 
import xml.etree.ElementTree as ET
from beautify import get_links
import os
from get_pdfs import get_pdfs


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly'] 
LABEL_NAME = "Papers"

def get_creds():
    creds = None

    if os.path.exists('token.json'): 
        with open('token.json', 'rb') as token: 
            creds = pickle.load(token) 

    if not creds or not creds.valid: 
        if creds and creds.expired and creds.refresh_token: 
            creds.refresh(Request()) 
        else: 
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES) 
            creds = flow.run_local_server(port=8080) 

        with open('token.json', 'wb') as token: 
            pickle.dump(creds, token)
            
    return creds

def get_label_id(label_name):
    """Get the ID of a label by its name."""
    creds = get_creds()
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    for label in labels:
        if label['name'] == label_name:
            print(f"Label ID: {label['id']}\n")
            return label['id']
    return None

def get_email_ids():
    """Get emails by label name."""
    creds = get_creds()
    service = build('gmail', 'v1', credentials=creds)
    label_id = get_label_id(LABEL_NAME)
    if not label_id:
        print(f"No label found with the name: {LABEL_NAME}")
        return []

    results = service.users().messages().list(userId='me', labelIds=[label_id]).execute()
    messages = results.get('messages', [])
    ids = [item['id'] for item in messages]
    print(f"Emails with ID: {label_id}")
    for id in ids:
        print("id: " + id)
    print("\n")
    return ids

def get_links_from_email(): 
    creds = get_creds()

    service = build('gmail', 'v1', credentials=creds) 

    ids = get_email_ids()

    for id in ids:    
        try: 
            response = service.users().messages().get(userId='me', id=id, format="raw").execute() 
            data = response["raw"]
            data = data.replace("-","+").replace("_","/") 
            decoded_data = base64.b64decode(data).decode('utf-8')
            links = get_links(decoded_data)
            for link in links:
                # print(f"{link}\n")
                with open("links.txt", "a") as f:
                    f.write(link + "\n")
        except Exception as e: 
            print(e)
    
    return links

if __name__ == "__main__":
    get_links_from_email()


