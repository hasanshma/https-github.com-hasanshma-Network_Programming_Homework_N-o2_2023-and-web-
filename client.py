import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("localhost",80))
for i in range(3):
    question=client_socket.recv(1024)
    print(question.decode())
    answer=input("> ")
    client_socket.send(answer.encode())
final_grade=client_socket.recv(1024)
print(final_grade.decode())
client_socket.close()
