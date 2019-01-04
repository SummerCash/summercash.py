import grpc

def LoadCert():
    with open("certs/new/termCert.pem", "rb") as f:
        return f.read()

def LoadKey():
    with open("certs/new/termKey.pem", "rb") as f:
        return f.read()

print(LoadCert())
print(LoadKey())

credentials = grpc.ssl_channel_credentials(
    private_key=LoadKey(),
    certificate_chain=LoadCert()
)