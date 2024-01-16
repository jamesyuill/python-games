from cryptography.fernet import Fernet


def load_key():
    file =  open('key.key','rb')
    key = file.read()
    file.close()
    return key



master_pwd = input('what is the master password? ')

key = load_key() + master_pwd.encode()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()

    with open("key.key", 'wb') as key_file:
        key_file.write(key)
'''


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #strips of carridge return
            user, passw = data.split(' | ')
            print("User:", user, ',| Password:', str(fer.decrypt(passw.encode())))



def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + str(fer.encrypt(pwd.encode())) + '\n')



while True:
    mode = input('would you like to add a new password or view existing ones? (view/add or press q to quit) ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid input')
        continue
