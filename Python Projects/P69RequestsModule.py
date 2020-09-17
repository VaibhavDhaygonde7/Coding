import requests
r = requests.get("http://vaibhav7.in/index.html")
print(r.text)         #this will print the html code of the url
# ther is also a function named r.status_code

url = "www.something.com"
data = {
    "p1":1,
    "p2":2
}
r2 = requests.post(url=url, data=data)
print(r2.text)