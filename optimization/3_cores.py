import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count

def get_links():
    curr_list = 'https://en.wikipedia.org/wiki/List_of_circulating_currencies'
    all_links = []
    response = requests.get(curr_list)
    soup = BeautifulSoup(response.text, "lxml")
    curr_el = soup.select('//table[1]/tbody/tr/td[2]/a')
    for link_el in curr_el:
        link = link_el.get("href")
        link = urljoin(curr_list, link)
        all_links.append(link)
    return all_links

def fetch(link):
    response = requests.get(link)
    with open("./output/"+link.split("/")[-1]+".html", "wb") as f:
        f.write(response.content)
    print('.',end='',flush=True)

if __name__ == '__main__':
    links = get_links()
    print(f"Total pages: {len(links)}")
    start_time = time.time()
    with Pool(cpu_count()) as p:
        p.map(fetch, links)

    duration = time.time() - start_time
    print(f"Downloaded {len(links)} links in {duration} seconds")
    #18.11