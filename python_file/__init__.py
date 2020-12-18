import requests
import bs4
import pandas as pd

products_link = []
dict_data_list = []

def get_product_link(page):
    print('Page: ',page)
    url = 'https://www.orami.co.id/shopping/category/aktivitas-bayi-bepergian?page='+ str(page)
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, features="html.parser")
    i=1
    for link in soup.find_all('div', class_="bottom-m-md"):
        p_links = 'https://www.orami.co.id' + link.find('a')['href']
        dict_link = {
            'Product Link': p_links
        }
        products_link.append(dict_link)
        print(i,p_links)
        i+=1

    if products_link == []:
        print("No more products")
        # print('Total products: ',len(products_link))
        return
    df1 = pd.DataFrame(products_link)
    df1.to_csv('/media/data/remoteworkerid/python/scraping_orami/csv_file/Link_products_page-'+ str(page) +'.csv',index=False,encoding='utf-8')

def detail_products(page):
    i=1
    for link in products_link:
        response = requests.get(link['Product Link'])
        soup = bs4.BeautifulSoup(response.text,features="html.parser")
        products_name = soup.find('h1',attrs={'class': 'prod-detail-title mb-8 loading'}).text
        print(i,products_name)
        price = soup.find('div',attrs={'class': 'prod-detail-price loading'}).text
        # print(price)
        stock = soup.find('div',attrs={'class': 'd-flex prod-detail-stock ml-auto loading'}).text
        # print(stock)
        image = soup.find('meta', attrs={'property': 'og:image'})['content']
        # print(image)
        prod_link = link['Product Link']
        dict_data = {
            'Product name' : products_name,
            'Price': price,
            'Stock': stock,
            'Image': image,
            'Link': prod_link
        }
        dict_data_list.append(dict_data)
        # if i==3:
        #     break
        i+=1
    # print(dict_data_list)
    df2 = pd.DataFrame(dict_data_list)
    df2.to_csv('/media/data/remoteworkerid/python/scraping_orami/csv_file/Detail_products_page-'+ str(page) +'.csv', index=False, encoding='utf-8')

if __name__ == '__main__':
    page = 17
    get_product_link(page)
    while products_link != []:
        detail_products(page)
        page+=1
        products_link.clear()
        dict_data_list.clear()
        get_product_link(page)
