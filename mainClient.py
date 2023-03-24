import socket

PORT = 666
HOST = "127.0.0.1"

expr = input('Ingrese la expresion matematica a evaluar: \n')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Converts the string into a byte string consisting of integers between 0 and 255
    s.sendall(bytes(expr, encoding='utf8'))
    data = s.recv(1024).decode('utf8')

print('El resultado es:')
print(data)

s.close()
