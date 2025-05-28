import json
import urllib.parse, urllib.request, urllib.error
import ssl

url = input("Enter URL: ")
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with urllib.request.urlopen(url, context=ctx) as response:
        data = response.read().decode()
except urllib.error.URLError as e:
    print(f"Error opening URL: {e.reason}")

info = json.loads(data)
info = info['comments']
nums = list()
#print (info)
print('User count:', len(info))

for item in info:
    item = int(item['count'])
    nums.append(item)
print ("The Sum is:", sum(nums))

