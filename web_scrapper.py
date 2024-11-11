import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Try to find the element by specific class
data = soup.find('div', class_='content')
if data:
    print("Found 'content' div:", data.text.strip())
else:
    print("Element with class 'content' not found. Trying other elements...")

    # Attempt other elements in case 'content' is not found
    alternatives = [
        ('div', 'main'), 
        ('div', 'container'), 
        ('div', 'page-content'), 
        ('section', None), 
        ('p', None),
        ('h1', None)
    ]
    
    for tag, class_name in alternatives:
        if class_name:
            element = soup.find(tag, class_=class_name)
        else:
            element = soup.find(tag)
        
        if element:
            print(f"Found '{tag}' with class '{class_name}':", element.text.strip())
            break
    else:
        print("No alternative elements found with content.")

# Alternative: Use a CSS selector to try multiple elements in one go
elements = soup.select('div.content, div.main, div.container, section, p, h1')
if elements:
    print("Found content using CSS selector:", elements[0].text.strip())
else:
    print("No elements found using CSS selector.")
