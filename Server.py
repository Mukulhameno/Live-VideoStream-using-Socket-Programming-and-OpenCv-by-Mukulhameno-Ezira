

import socket,cv2,pickle,struct

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip=socket.gethostname()
print('HOST IP:',host_ip)
port=3000
socket_address=(host_ip,port)

server_socket.bind(socket_address)

server_socket.listen(5)
print("LISTENING AT:",socket_address)

while True:
    client_socket,addr=server_socket.accept()
    print('GOT CONNECTION FROM:',addr)
   # with open(filename,'wb') as handle:
   #     pickle.dump(data,handle,protocol=pickle.HIGHEST_PROTOCOL)
    if client_socket:
        vid=cv2.VideoCapture(0)
        while(vid.isOpened()):
            img,frame=vid.read()
            a=pickle.dumps(frame)
            message=struct.pack("Q",len(a))+a
            client_socket.sendall(message)
            cv2.imshow('TRANSMITTING VIDEO',frame)
            key=cv2.waitKey(13) & 0xFF
            if key ==ord('q'):
                client_socket.close()
                break
cv2.destroyAllWindows()
                
