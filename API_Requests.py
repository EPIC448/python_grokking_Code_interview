# import API_Requests
import requests # ignore the Line. this works now.
import json

#  Resources  https://www.dataquest.io/blog/python-api-tutorial/
#  ran command:  npm install requests


response = requests.get("https://jsonplaceholder.typicode.com/comments")
print(response.json())


#  Query API with out any method in Python. 
print("Check this iourl")

