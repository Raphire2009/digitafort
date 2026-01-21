import requests 


"""  getting the data from the a site vai api """

#creating the request for the data 
#check the status code 
# print request data
res = requests.get("https://jsonplaceholder.typicode.com/users")

if res.status_code == 200:
    data = res.json()
    print(f"our data is {data}")
else:
    print(f"Erro Message: {res.status_code}")
