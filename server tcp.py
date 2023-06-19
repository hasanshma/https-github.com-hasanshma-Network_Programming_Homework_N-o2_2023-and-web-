import socket
import threading
import json
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("localhost",80))
server_socket.listen()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
print ("Server is running")
grades={}
def handle_client(client_socket,client_address):
    print(f"Connected with{client_address}")
    grades[client_address]=0 
    with open("quiz.json","r") as file:
        questions = json.load(file)  
    '''questions={
        "whats the port of http?":"80",
        "whats the port of https?": "443",
        "whats the port of ftp?":"53"}'''
    for question,answer in questions.items():
        client_socket.send(question.encode())
        client_answer=client_socket.recv(1024).decode()
        if client_answer.strip().lower()==answer.lower():
            grades[client_address]+=1
    client_socket.send(f"your final grade is {grades[client_address]}/3".encode())
    client_socket.close()
while True:
    client_socket,client_address=server_socket.accept()
    print("client connected from : ",client_address)
    client_thread=threading.Thread(target=(handle_client(client_socket, client_address)),args=(client_socket,client_address))
    client_thread.start()


 