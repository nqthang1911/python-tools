import requests
'''
response = requests.get('https://api.github.com/')
print('status_code:',response.status_code)
print(response.json()['current_user_url'])

#headers
print('headers:',response.headers['Content-Type'])
'''

'''
url = 'https://api.github.com/search/repositories?q=requests+language:python'
response = requests.get(url)
print(response.json()['total_count'])
'''

#demo 3 ~> thay đổi headers requests
'''
import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')
'''

'''
#demo form-data 
response = requests.post('https://httpbin.org/post', data={'name':'thangit','age':37})
print(response.text)
'''

#demo json
'''
response = response = requests.post('https://httpbin.org/post', json={'name':'thang','age':20})
print(response.text)
'''

#demo proxies
'''
proxies = {
    'http':'http://operator:operator@113.161.210.88:1080/',
    'https':'http://operator:operator@113.161.210.88:1080/'
}

response = requests.get('https://api.myip.com',proxies=proxies)
print(response.json())
myip = response.json()['ip']
print(myip)
'''

proxies = {
    'http':'http://Anonymous:Anonymous@77.72.3.163:80/',
    'https':'https://Anonymous:Anonymous@77.72.3.163:80/'
}

response = requests.get('https://api.myip.com',proxies=proxies)
print(response.json())
myip = response.json()['ip']
print(myip)