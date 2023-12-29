import requests
import json
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import Border
from openpyxl.styles import Side
from openpyxl.styles import PatternFill
from selenium import webdriver

'''
1. User can input search terms and script will automatically look for it in Lazada
2. Results will be saved in an .xlsx file
3. File will be saved locally, but have functionality to be saved in email
4. Script will look for four pages
5. Script will have usable UI
'''
search = input(f'Enter item name: ').replace(' ', '-')

url = f'https://www.lazada.com.ph/tag/{search}'
# page_number = input(f'How many pages do you want to search? ')

browser = webdriver.Chrome()

root = 'https://lazada.com.ph'

browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, features = 'html.parser')

wb = Workbook()
worksheet = wb['Sheet']

product_name_list = []
product_price_list = []
product_link_list = []

def find_product():
    products = soup.find_all('div', class_ = 'Bm3ON')

    for product in products:
        product_name = product.find('div', class_ = 'RfADt')
        product_price = product.find('span', class_ = 'ooOxS')
        product_link = product.a['href']

        product_name_list.append(product_name.text)
        product_price_list.append(product_price.text.replace('₱', ''))
        product_link_list.append(product_link)

        # print(f'Product name: {product_name.text}')
        # print(f'Price: {product_price.text}')
        # print(f'Product link: {product_link}\n')

succeeding_pages = soup.find_all('li', title = True)

def find_product_succeeding_pages():

    for page in succeeding_pages:
        page_link = page.find('a', href = True)
        if page_link is not None:
            browser.get(f'{root}/{page_link['href']}')
            html = browser.page_source
            soup = BeautifulSoup(html, features = 'html.parser')

            find_product()

def populate_sheet():
    for row, name in zip(worksheet.iter_rows(min_row = 1, max_row = len(product_name_list)), product_name_list):
        for cell in row:
            cell.value = name

    for row, price in zip(worksheet.iter_rows(min_row = 1, max_row = len(product_name_list), min_col = 2, max_col = 2), product_price_list):
        for cell in row:
            cell.value = price

    for row, link in zip(worksheet.iter_rows(min_row = 1, max_row = len(product_name_list), min_col = 3, max_col = 3), product_link_list):
        for cell in row:
            cell.value = link

if __name__ == '__main__':
    find_product()
    find_product_succeeding_pages()
    populate_sheet()

wb.save('laz-results.xlsx')