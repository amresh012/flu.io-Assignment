import requests
from bs4 import BeautifulSoup
import re

def extract_social_links(soup):
    social_links = []
    social_patterns = [r"facebook\.com", r"twitter\.com", r"instagram\.com"]
    
    for link in soup.find_all("a", href=True):
        for pattern in social_patterns:
            if re.search(pattern, link["href"], re.IGNORECASE):
                social_links.append(link["href"])
                break
    
    return social_links

def extract_email_addresses(text):
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    emails = re.findall(email_pattern, text)
    return emails

def extract_contact_details(text):
    contact_pattern = r"(\+?\d{0,2}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{2,5}[-.\s]?\d{2,5})"
    contacts = re.findall(contact_pattern, text)
    return contacts

def main():
    website_url = input("Enter the website URL: ")
    
    try:
        response = requests.get(website_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        social_links = extract_social_links(soup)
        email_addresses = extract_email_addresses(response.text)
        contact_details = extract_contact_details(response.text)
        
        print("\nSocial Links:")
        for link in social_links:
            print(link)
        
        print("\nEmail Addresses:")
        for email in email_addresses:
            print(email)
        
        print("\nContact Details:")
        for contact in contact_details:
            print(contact)
    
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
