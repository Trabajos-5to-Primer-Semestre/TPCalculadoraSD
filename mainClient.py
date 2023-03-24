import socket

PORT = 666
HOST = "127.0.0.1"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Converts the string into a byte string consisting of integers between 0 and 255

    run = 'yes'

    while run != 'no':

        expr = input('Ingrese la expresion matematica a evaluar: \n')

        s.sendall(bytes(expr, encoding='utf8'))
        data = s.recv(1024).decode('utf8')

        print(f'El resultado es: {data}')

        run = input('Desea realizar otro calculo? [si/no]: \n')
        if run == 'no':
            s.sendall(bytes(run, encoding='utf8'))

