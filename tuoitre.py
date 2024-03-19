import os
import requests
from bs4 import BeautifulSoup
import random


def crawl_bongda_content(url):
    try:
        # Gửi yêu cầu HTTP để lấy HTML từ trang web
        response = requests.get(url)
        response.raise_for_status()

        # Sử dụng BeautifulSoup để phân tích cú pháp HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trích xuất nội dung bài báo
        article_content = soup.find('div', class_='exp_content news_details')
        if article_content:
            # Lấy tiêu đề bài báo
            nguon_index = article_content.get_text().find('Nguồn:')
            if nguon_index != -1:
                article_content = article_content.get_text()[:nguon_index]
                
            title = soup.find('h1', class_="time_detail_news").get_text()

            # Lưu nội dung vào file trong thư mục
            return article_content
        else:
            print( "Không tìm thấy nội dung bài báo.")
            return ""
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)
        
def crawl_tuoitre_content(url):
    try:
        # Gửi yêu cầu HTTP để lấy HTML từ trang web
        response = requests.get(url)
        response.raise_for_status()

        # Sử dụng BeautifulSoup để phân tích cú pháp HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trích xuất nội dung bài báo
        article_content = soup.find('div', class_='detail-content afcbc-body')
        if article_content:
            # Lấy tiêu đề bài báo
            nguon_index = article_content.get_text().find('Nguồn:')
            if nguon_index != -1:
                article_content = article_content.get_text()[:nguon_index]
                
            title = soup.find('h1', class_="detail-title").get_text()

            # Lưu nội dung vào file trong thư mục
            return article_content
        else:
            print( "Không tìm thấy nội dung bài báo.")
            return ""
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Error:", err)
