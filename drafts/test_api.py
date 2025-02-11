import requests
# blowfish_id
response = requests.get("https://api.juggler.develop.blowfish.api4ftx.cloud/transactions/view?id=f090beb6-cf00-466a-86e2-d9edd8c28121")
print(response.text)

# external_id
response = requests.get("https://api.juggler.develop.blowfish.api4ftx.cloud/transactions/search?id=20daad40-cba4-4687-a287-85e0e975dee5")
print(response.text)