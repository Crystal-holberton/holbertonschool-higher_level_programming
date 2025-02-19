#!/usr/bin/python3
"""Python script to fetch posts from JSONPlaceholder"""
import requests
import csv


def fetch_and_print_posts():
    """Send request to JSONPlaceholder"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for resp in data:
            title = resp["title"]
            print(title)
    else:
        print("Request was not successful.")


def fetch_and_save_posts():
    """Save response data to a dictionary"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        csvf = 'posts.csv'
        datalist = []
        for element in data:
            post = {
                'id': element.get('id'),
                'title': element.get('title'),
                'body': element.get('body')
            }
            datalist.append(post)
        with open(csvf, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(datalist)
    else:
        print("request was not successful.")
