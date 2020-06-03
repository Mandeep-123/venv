To get repostory list of a user

import requests
username = input("Enter the github username:")
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
for i in range(0,len(json)):
  print("Number:",i+1)
  print("Repository Name:",json[i]['name'])
  print("Repository URL:",json[i]['svn_url'],"\n")