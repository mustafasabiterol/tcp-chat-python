import socket, threading

HOST, PORT = "0.0.0.0", 65432
clients = []                     # bağlı soketler

def echo_to_others(me):
    while True:
        msg = me.recv(1024)
        if not msg:
            break
        for c in clients:        # aynı mesajı herkese dağıt
            if c is not me:
                c.sendall(msg)
    clients.remove(me)
    me.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server {PORT} portunda hazır…")
    while True:
        conn, _ = s.accept()
        clients.append(conn)
        threading.Thread(target=echo_to_others,
                         args=(conn,), daemon=True).start()
