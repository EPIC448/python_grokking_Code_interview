# import API_Requests
import requests # ignore the Line. this works now.
import json

#  Resources  https://www.dataquest.io/blog/python-api-tutorial/
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/   how to query API properly.
#  ran command:  npm install requests

query ={"postId": 5 } # How to add a parameter into your query. very important.
response = requests.get("https://jsonplaceholder.typicode.com/comments",params= query)
# here, there may be some Iteration happening
print(response.json())


#  Query API with out any method in Python. 
print("Check this iourl")

