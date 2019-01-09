import sys
class Server:
    def __init__(self, ip, port):
        self.rawIP = ip
        self.port = port
        try:
            self.ip = rawIP + ":" + str(port)
        except:
            print("invalid port number")
            sys.exit(-1)
    


if __name__ == "__main__":
    server = Server(
        ip="localhost",
        port=8080
    )
    accounts = accounts.Accounts(server)
    r = accounts.CallMethod("NewAccount", "", "")
    print(r)
