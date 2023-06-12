import json

def loadData(filename):
    with open(filename, 'w+') as file:
        try:
            data = json.loads(file.read())
        except:
            data = list()
            print('empty json!')
    return data

def saveData(filename, data):
    with open(filename, 'w') as file:
        file.write(json.dumps(data))

def main():
    users = loadData('users.json')
    usersData = loadData('usersData.json')
    usersPasswords = loadData('usersPasswords.json')
    
    if not type(users) and not type(usersData) and not type(usersPasswords):
        print(f'can\'t load data cause one of parameters is None : \n users : {type(users) is not None} \n usersData : {type(usersData) is not None} \n usersPasswords : {type(usersPasswords) is not None}')
        exit(-1)
    
    users.append('Vlad')
    usersData.append({
        'name' : 'Vlad',
        'surname' : 'Vickers'
    })
    usersPasswords.append('love my dog')

    saveData('users.json',users)
    saveData('usersData.json',usersData)
    saveData('usersPasswords.json',usersPasswords)
