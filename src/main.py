import requests
import json

def main():
    url = "https://localhost:8080/twirp/common.Common/DecodeString"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "DecodeString",
        "params": ["hello world"],
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()
    print(response)

    # assert response["result"] == "echome!"
    # assert response["jsonrpc"]
    # assert response["id"] == 0

if __name__ == "__main__":
    main()