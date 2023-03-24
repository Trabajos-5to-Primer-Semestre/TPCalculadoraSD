import socket

PORT = 6666
HOST = "127.0.0.1"

# Creates socket class element specifying the address family and socket type
# Socket_stream = TCP / IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connects to the socket
    s.connect((HOST, PORT))

    run = 'yes'

    while run != 'no':

        expr = input('Ingrese la expresion matematica a evaluar: \n')

        # Serialize the user input to be sent into bytes and then we send it
        expr = bytes(expr, encoding='utf8')
        s.sendall(expr)

        # The data is received and deserialized
        data = s.recv(1024).decode('utf8')

        print(f'El resultado es: {data}')

        run = input('Desea realizar otro calculo? [si/no]: \n')
        if run == 'no':
            s.sendall(bytes(run, encoding='utf8'))
