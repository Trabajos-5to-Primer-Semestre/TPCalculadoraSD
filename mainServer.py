import numexpr
import socket

PORT = 666

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Binds an IP address and a port number to a socket instance and since the IP is empty it takes all ips
    s.bind(('', PORT))
    # Listens for connection attempts
    s.listen()
    # Accepts the socket connection
    conn, addr = s.accept()

    with conn:  # With the open connection
        print(f"Connected by {addr}")

        while True:

            data = conn.recv(1024)
            data = str(data.decode('utf-8'))
            print(data)
            if data == 'no':
                print("Apagando servidor...")
                break

            data = str(numexpr.evaluate(data.replace('^', '**')))
            data = bytes(data, encoding='utf8')

            conn.sendall(data)


