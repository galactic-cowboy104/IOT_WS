import socket 
import sys

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    mysocket.bind(('0.0.0.0', 1234))
except socket.error:
    print('Failed to bind.')
    sys.exit()

mysocket.listen(5)

try:

    while True:
        
        conn, addr = mysocket.accept()
        data = conn.recv(1024)

        if not data:
            break
        else: 

            print('Got a request!')

            response = 'HTTP/1.1 200 OK\n\nGot a request!\n'

            conn.sendall(response.encode())

        conn.close()

except KeyboardInterrupt:
    pass

finally:
    mysocket.close()  