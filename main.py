
clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    if  client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')

def list_clients():
    global clients
    print(clients)

def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print('Client not found')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name+',', '')
    else:
        print('Client not found')


def _add_comma():
    global clients
    clients += ','
    
def _print_welcome():
    print('WELCOME')
    print('*'*40)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')

def _get_client_name():
    return input('what is the client name?')

if __name__=='__main__':
    _print_welcome()
    command = input().upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name_client = input('What is the updated client name?')
        update_client(client_name, updated_name_client)
        list_clients()
    else:
        print('Invalid command')
