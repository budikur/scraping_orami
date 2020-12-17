import requests
import bs4
import pandas as pd

products_link = []
products_link_perpage = []
dict_data_list = []

def get_product_link(page):
    print('Page: ',page)
    url = 'https://www.orami.co.id/shopping/category/aktivitas-bayi-bepergian?page='+ str(page)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    i=1
    for link in soup.find_all('div', class_="bottom-m-md"):
        p_links = 'https://www.orami.co.id' + link.find('a')['href']
        products_link.append(p_links)
        products_link_perpage.append(p_links)
        print(i,p_links)
        i+=1
    print(i)
    # print(products_link)
    if products_link_perpage == []:
        print("No more products")
        print('Total products: ',len(products_link))
        return
    products_link_perpage.clear()
    page+=1
    get_product_link(page)

def detail_products():
    i=1
    for link in products_link:
        response = requests.get(link)
        soup = bs4.BeautifulSoup(response.text,features="html.parser")
        # print(soup)
        products_name = soup.find('h1',attrs={'class': 'prod-detail-title mb-8'}).text
        print(products_name)
        # price = soup.find('div',attrs={'class': 'prod-detail-price  '})
        # print(price)
        # stock = soup.find('div',attrs={'class': 'd-flex prod-detail-stock ml-auto '}).text
        # print(stock)
        # image = soup.find('img')['src']
        # print(image)
        # # description =
        # dict_data = {
        #     'Product name' : products_name,
        #     'Price': price,
        #     'Stock': stock,
        #     'Image': image
        # }
        # dict_data_list.append(dict_data)
        # print(dict_data_list)
        if i==3:
            break
        i+=1

# def testing():
#     print('testing')

if __name__ == '__main__':
    page = 20
    get_product_link(page)
    detail_products()
    # testing()
