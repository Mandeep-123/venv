			All Commits:
For master  branch
import requests
r = requests.get('https://api.github.com/repos/Mandeep-123/book-practice/commits')
print(len(r.json()))
for i in range(0,len(r.json())):
    print(r.json()[i]['commit']['message'])



			Only Last commit:
Method -1 
r = requests.get('https://api.github.com/repos/Mandeep-123/book-practice/git/refs/heads/master')
print(r.json())

Method -2
import requests 
repo = 'Mandeep-123/book-practice'

r = requests.get('https://api.github.com/repos/{0}/commits?per_page=1'.format(repo))

commit = r.json()[0]["commit"]

print(commit)