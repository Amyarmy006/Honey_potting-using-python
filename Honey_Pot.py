import socket
import logging

logging.basicConfig(
    filename="Honey_pot_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def main():
    ip = '192.168.36.129'
    port = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(10)
    print("Honey Potting started!")

    try:
        while True:
            client_con, client_add = s.accept()
            print(f"Connection occurred from {client_add}")
            logging.info(f"Connection occurred from {client_add}")
            client_con.send(b"<h1>You have been spotted!</h1>")
            data = client_con.recv(2048)
            print(data.decode('utf-8'))
            logging.info(data.decode('utf-8'))

    except Exception as identifier:
        print(f"Unspecified Error Occurred: {identifier}")
        s.close()
    except KeyboardInterrupt:
        print("Honey Potting Process Stopped!")        
        s.close()

if __name__ == "__main__":
    main()
