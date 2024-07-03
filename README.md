# BytePost

`BytePost` is a versatile Python module that supports sending HTTP requests using multiple libraries: `aiohttp`, `requests`, and `tls_client`. It allows you to perform HTTP operations such as `GET`, `POST`, `PUT`, and `DELETE` and save the responses in a pretty-printed JSON format.

## Features

- Asynchronous requests using `aiohttp`
- Synchronous requests using `requests` and `tls_client`
- Supports multiple HTTP methods: `GET`, `POST`, `PUT`, `DELETE`
- Saves responses in a pretty-printed JSON format
- Supports proxies

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/bytepost.git
    cd bytepost
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Example Usage

import asyncio
from bytepost import BytePost

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "foo", "body": "bar", "userId": 1}
proxy = None  # Example does not use a proxy

# Asynchronous POST request using aiohttp
async def main():
    bytepost = BytePost('aiohttp', 'post', url, payload)
    await bytepost.async_index()

# Synchronous POST request using requests
bytepost = BytePost('requests', 'post', url, payload)
bytepost.index()

# Synchronous POST request using tls_client
bytepost = BytePost('tls_client', 'post', url, payload)
bytepost.index()

# Run the async example
asyncio.run(main())

# Example of a synchronous GET request using requests
bytepost_get = BytePost('requests', 'get', url)
bytepost_get.index()

# Example of an asynchronous GET request using aiohttp
async def main_get():
    bytepost = BytePost('aiohttp', 'get', url)
    await bytepost.async_index()

asyncio.run(main_get())

# Example of a synchronous GET request using tls_client
bytepost_tls_get = BytePost('tls_client', 'get', url)
bytepost_tls_get.index()
