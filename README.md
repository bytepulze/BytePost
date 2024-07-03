# BytePost

`BytePost` is a versatile Python module that supports sending HTTP requests using multiple libraries: `aiohttp`, `requests`, and `tls_client`. It allows you to perform HTTP operations such as `GET`, `POST`, `PUT`, and `DELETE` and save the responses in a pretty-printed JSON format.

## Features

- Asynchronous requests using `aiohttp`
- Synchronous requests using `requests` and `tls_client`
- Supports multiple HTTP methods: `GET`, `POST`, `PUT`, `DELETE`
- Saves responses in a pretty-printed JSON format
- Supports proxies

## Example Usage
```py
from bytepost import BytePost

payload = {"content": "@everyone bytepost is js better", "username": "BytePost", "icon_url": "https://media.discordapp.net/attachments/1257622093692932127/1258043752031719505/image.png?ex=66869c0b&is=66854a8b&hm=49653b55428e352a5dae5962fb5fe37e6eeba26a9a8824ea3b758996ff817274&=&format=webp&quality=lossless&width=490&height=104"}
webhook = "https://discord.com/api/webhooks/1258043203719004322/Yj7rpl7-TaZsHT_7zwyhbn9vPFTs3hUWzuBMeayzLuk2iVVQQYM8NPdMK5XT9Tt-UJic"

def index(webhook, payload):
    post = BytePost(method="tls_client", http_method="post", url=webhook, payload=payload)
    post.index()

index()
```

## Example Response
![image](https://github.com/bytepulze/BytePost/assets/153377701/6e6ef326-3257-4656-8353-8031e0f95170)
