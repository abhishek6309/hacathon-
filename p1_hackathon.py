import requests
import re
import urllib.parse as urlparse

target_url="https://crawltest1.forenzy.net/"
target_links = []

def extract_urls(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"',response.content.decode(errors="ignore"))

def crwal(url):

    all_links = extract_urls(url)
    for link in all_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]


        if target_url in link and link not in target_links:
             target_links.append(link)
             print(link)
             crwal(link)



crwal(target_url)


with open('output.txt', 'w') as f:
    for line in target_links:
        f.write(line)
        f.write('\n')


