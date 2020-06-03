#to get the list of files and folders in master branch

import requests
repo = 'Mandeep-123/book-practice'

r = requests.get('https://api.github.com/repos/{0}/commits?per_page=1'.format(repo))

commit = r.json()[0]["commit"]['tree']['url']
r=requests.get(commit)
print(len(r.json()['tree']))
for i in range(0,len(r.json()['tree'])):
    print(r.json()['tree'][i]["path"])
    print("--------\n")

print(commit)