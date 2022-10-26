import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
temp = r"C:\Users\HP\Desktop\web\temp"
redirect = '127.0.0.1'
websites = ['www.pornhub.com', '.pornhub.com', 'www.xhamster.com', 'xhamster.com', 'www.xnxx.com', 'www.xnxx.com', 'www.redtube.com', '.redtube.com']
with open(hosts_path, "r+") as file:
    content = file.read()
    for website in websites:
        if website not in content:
            file.write(redirect + '      ' + website + "\n")


