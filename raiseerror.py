users={'paras':'p123',
       'ashu':'a456',
       'neha':'n654'}

class LoginError(Exception):
    pass
def login(user,pwd):
    if user in users and users[user]==pwd:
        print(f'{user} Welcome')
    else:
        raise LoginError()

while True:
    try:
        uname=input("UserName:")
        pwd=input("Password:")
        login(uname,pwd)
        break
    except LoginError:
        print("invalid username or password")
