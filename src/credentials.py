import grpc

def LoadCert():
    with open("certs/new/xoreo99Cert.pem", "rb") as f:
        return f.read()

def LoadKey():
    with open("certs/new/xoreo99Key.pem", "rb") as f:
        return f.read()

print(LoadCert())
print(LoadKey())
credentials = grpc.ssl_channel_credentials(

    private_key=LoadKey(),
    certificate_chain=LoadCert()
)