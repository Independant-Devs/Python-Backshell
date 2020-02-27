import socket

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter the target IP  #")
port = int(input("Enter the connecting port  #"))
connexion.connect((host, port))
print("Connection to " + host + " in " + str(port) + " realized !")
started = True

if started == True:
    choice = int(input("1: Send a command\n2: Exit\n[root@" + host + "] $"))
    if choice == 1:
        command = input("[" + host + "@cmd.exe] $")
        connexion.send(command.encode())
        retour = connexion.recv(1024).decode('latin1')
        print(retour)
    if choice == 2:
        connexion.send(b"exit")
        connexion.close()
        exit
        
    
