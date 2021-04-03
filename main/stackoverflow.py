# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:44:18 2021

@author: LEEKWANGJIN
"""

import requests
from bs4 import BeautifulSoup



URL = f"https://stackoverflow.com/jobs?q=python&sort=1"

result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
pagination = soup.find("div", {"class" : "pagination"})


def get_last_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class" : "pagination"}).find_all("a")
    print(pages)

def get_jobs():
    last_page = get_last_pages()
    return []
    
    
    