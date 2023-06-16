import requests

headers = {
    "User-Agent": "windows",
    "Referer": "http://www.nate.com"


}

response = requests.get("http://m.nate.com", 
                        verify=False, 
                        headers=headers, 
                        allow_redirects=False)


fd = open('b.html', "wb")
fd.write(response.content)
fd.close()


# if "Location" in response.headers or response.status_code == 302:
#     response2 = requests.get(response.headers["Location"], verify=False, headers= headers)