import requests
import config
import time
from datetime import datetime
import threading
import queue

class CacheHandler:
    urls = queue.Queue()
    response = queue.Queue()

    def __init__(self, nb_threads):
        self.nb_threads = nb_threads

    def run(self, urls):
        for i in range(0, self.nb_threads):
            threading.Thread(target=self.fetch_data, args=(urls,)).start()
            threading.Thread(target=self.store).start()
            threading.Thread(target=self.expire, args=(10, 2,)).start()

    def fetch_data(self, urls):
        '''
            Function that is used to request the data from the server for the URL provided and store the data in a queue
        :param urls: URLs to fetch the data from the server
        :return: None
        '''

        for url in urls:
            print("FETCHING DATA")
            self.urls.put(url)
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    response_text = response.text
                    self.response.put(response_text)
                    print("DATA FETCHED SUCCESS!")
                else:
                    print("DATA FETCHED UNSUCCESSFUL")
            except:
                print("NOT ABLE TO SEND REQUEST TO THE SERVER")

    def store(self):
        '''
            Function to store data in cache
        :return: None
        '''
        while not self.urls.empty():
            time.sleep(0.2)
            print("STORING THE DATA IN CACHE")
            url = self.urls.get()
            response_value = self.response.get()
            config.cache[url] = (response_value, datetime.now())
            print("DATA STORED IN CACHE")
            print("*" * 50)
            print(config.cache)
            print("*" * 50)

    def expire(self, timeout=10, delay_sec=1):
        '''
            Funtion to expire or delete the data from the cache
        :param expire_time: time limit for the data store in the cache
        :param delay_sec: defining the time to check for the expiry of the data in cache
        :return: None
        '''
        while 1:
            time.sleep(delay_sec)
            print("EXPIRING A KEY-VALUE PAIR FROM CACHE")
            try:
                for key in [key for key, value in config.cache.items() if (datetime.now() - value[1]).total_seconds() >= timeout]: del config.cache[key]
            except:
                print("CACHE EXPIRATION SUCCESS")
            print("*"*50)
            print(config.cache)
            print("*" * 50)

    def get(self, user_url):
        '''
            Function to get the data from the cache server if exists otherwise get the data from the actual server
        :param user_url: URL to fetch the data from the server
        :return: a value from a python dictionary
        '''

        try:
            print("Getting the data requested by the user...")
            if user_url not in config.cache:
                print("DATA NOT IN CACHE")
                print("STORING DATA IN CACHE")
                self.fetch_data(user_url)
            return config.cache[user_url]
        except:
            print("DATA NOT IN CACHE. FETCHING DATA FROM THE SERVER")

if __name__ == "__main__":
    ch = CacheHandler(nb_threads=4)
    ch.run(config.links)
    for link in config.links:
        time.sleep(0.5)
        print("GETTING THE DATA")
        response_value = ch.get(link)
        print("RESPONSE::\n", response_value)
    print("Cache::\n\n", config.cache)