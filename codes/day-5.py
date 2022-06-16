datas=[
    {
        "username": "deepak",
        "password": "dk123",    
        'props':{
            "name":"deepak",
            "age":20,
            "address":"lakhe nagar"
            }
    },
    {   
        "username": "lokesh",
        "password": "lk123",
        "props":{
            "name":"lokesh",
            "age":20,
            "address":"raipura"
            }
    }
]

username=input("enter the username:")
password=input("enter the password:")
for data in datas:
    if(username == data['username']):
        if(password == data['password']):
            print("props", data['props'])