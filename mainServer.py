import numexpr
import socket

PORT = 6666

# Creates socket class element specifying the address family and socket type
# Socket_stream = TCP

print('Inicializando socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Binds an IP address and a port number to a socket instance and since the IP is empty it takes all ips
    s.bind(('127.0.0.1', PORT))
    # Listens for connection attempts
    s.listen()

    while True:
        # Accepts the socket connection
        conn, addr = s.accept()

        with conn:  # With the open connection
            print(f"Connected by {addr}")

            while True:
                # Receive the socket message, specifying the max amount of data
                data = conn.recv(1024)
                # The received data is then deserialized into a string
                data = str(data.decode('utf-8'))
                print(data)
                if data == 'no':
                    print("Cerrando conexion...")
                    break

                # Perform the calculations needed
                data = str(numexpr.evaluate(data.replace('^', '**')))
                # Serialize the data for sending back to the client
                data = bytes(data, encoding='utf8')

                conn.sendall(data)


