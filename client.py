import socket, threading, sys

HOST, PORT = "127.0.0.1", 65432   # sunucu adresi

def listen(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            print("\n[Bağlantı kesildi]")
            sys.exit()
        print("\r↪ " + data.decode() + "\n> ", end="")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    threading.Thread(target=listen, args=(s,), daemon=True).start()
    print("Bağlısın. Çıkmak için 'exit' yaz.")
    while True:
        msg = input("> ")
        if msg.lower() == "exit":
            break
        s.sendall(msg.encode())
