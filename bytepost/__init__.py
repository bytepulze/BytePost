import tls_client
import requests
import aiohttp
import json
import asyncio
from threading import Thread
from colorama import *

class BytePost:
    def __init__(self, method, http_method, url, payload=None, headers=None, proxy=None):
        self.method = method.lower()
        self.http_method = http_method.lower()
        self.url = url
        self.payload = payload
        self.headers = headers
        self.proxy = proxy

    async def aiohttp_request(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            if self.http_method == 'post':
                async with session.post(self.url, json=self.payload, proxy=self.proxy) as response:
                    return await response.text()
            elif self.http_method == 'get':
                async with session.get(self.url, proxy=self.proxy) as response:
                    return await response.text()
            elif self.http_method == 'put':
                async with session.put(self.url, json=self.payload, proxy=self.proxy) as response:
                    return await response.text()
            elif self.http_method == 'delete':
                async with session.delete(self.url, proxy=self.proxy) as response:
                    return await response.text()
            else:
                raise ValueError("Unsupported HTTP method. Use 'get', 'post', 'put', or 'delete'.")

    def requests_request(self):
        if self.http_method == 'post':
            response = requests.post(self.url, json=self.payload, headers=self.headers, proxies={'http': self.proxy, 'https': self.proxy})
        elif self.http_method == 'get':
            response = requests.get(self.url, headers=self.headers, proxies={'http': self.proxy, 'https': self.proxy})
        elif self.http_method == 'put':
            response = requests.put(self.url, json=self.payload, headers=self.headers, proxies={'http': self.proxy, 'https': self.proxy})
        elif self.http_method == 'delete':
            response = requests.delete(self.url, headers=self.headers, proxies={'http': self.proxy, 'https': self.proxy})
        else:
            raise ValueError("Unsupported HTTP method. Use 'get', 'post', 'put', or 'delete'.")
        return response.text

    def tls_client_request(self):
        session = tls_client.Session(client_identifier="chrome_110")
        if self.http_method == 'post':
            response = session.post(self.url, json=self.payload, headers=self.headers, proxy=self.proxy)
        elif self.http_method == 'get':
            response = session.get(self.url, headers=self.headers, proxy=self.proxy)
        elif self.http_method == 'put':
            response = session.put(self.url, json=self.payload, headers=self.headers, proxy=self.proxy)
        elif self.http_method == 'delete':
            response = session.delete(self.url, headers=self.headers, proxy=self.proxy)
        else:
            raise ValueError("Unsupported HTTP method. Use 'get', 'post', 'put', or 'delete'.")
        return response.text

    def save_data(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    async def process_aiohttp(self):
        text = await self.aiohttp_request()
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = text
        self.save_data(data, f'{self.method}_{self.http_method}_aiohttpresult.json')
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}SUCCESS{Fore.LIGHTBLACK_EX}] {self.http_method.upper()}{Fore.RESET} Process Was Finished Successfully, URL Response Was Saved Into {Fore.LIGHTBLACK_EX}{self.method}_{self.http_method}_aiohttpresult.json")

    def process_requests(self):
        text = self.requests_request()
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = text
        self.save_data(data, f'{self.method}_{self.http_method}_requestsresult.json')
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}SUCCESS{Fore.LIGHTBLACK_EX}] {self.http_method.upper()}{Fore.RESET} Process Was Finished Successfully, URL Response Was Saved Into {self.method}_{self.http_method}_requestsresult.json")

    def process_tls_client(self):
        text = self.tls_client_request()
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = text
        self.save_data(data, f'{self.method}_{self.http_method}_tlsclientresult.json')
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}SUCCESS{Fore.LIGHTBLACK_EX}] {self.http_method.upper()}{Fore.RESET} Process Was Finished Successfully, URL Response Was Saved Into {self.method}_{self.http_method}_tlsclientresult.json")

    def index(self):
        if self.method == 'aiohttp':
            asyncio.run(self.process_aiohttp())
        elif self.method == 'requests':
            thread = Thread(target=self.process_requests)
            thread.start()
            thread.join()
        elif self.method == 'tls_client':
            thread = Thread(target=self.process_tls_client)
            thread.start()
            thread.join()
        else:
            raise ValueError("Unsupported method. Use 'aiohttp', 'requests', or 'tls_client'.")
