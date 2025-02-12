import requests
# blowfish_id
# response = requests.get("https://api.juggler.develop.blowfish.api4ftx.cloud/transactions/view?id=f090beb6-cf00-466a-86e2-d9edd8c28121")
# print(response.text)

# # external_id
# response = requests.get("https://api.juggler.develop.blowfish.api4ftx.cloud/transactions/search?id=20daad40-cba4-4687-a287-85e0e975dee5")
# print(response.text)

res_response = {
    "data": [
        {
            "id": "20daad40-cba4-4687-a287-85e0e975dee5",
            "created_at": "2025-02-11 01:14:23",
            "updated_at": "2025-02-11 01:14:24",
            "type_id": 1,
            "type_text": "deposit",
            "state_id": 1,
            "state_text": "Created",
            "state_final": False,
            "participant_id": "404ae456-fb1d-4043-9e7b-a399f4d29cf3",
            "participant_name": "TestAurisAccount",
            "customer_id": "id-784693968623",
            "customer_payment_id": "449bc546-e589-4aca-83fd-879694134546",
            "source_amount_currency": "AZN",
            "source_amount_value": "6000.00",
            "destination_amount_currency": "AZN",
            "destination_amount_value": "0",
            "rate": "0",
            "rate_source_currency": "AZN",
            "rate_destination_currency": "AZN",
            "provider": "pay4u",
            "source_requisites": [
                {
                    "bank_name": "sberbank",
                    "card_holder": "Сбер Картович",
                    "card_number": "1112121111111112"
                }
            ]
        }
    ],
    "success": True
}

item = res_response["data"][0]['id']
bank_name = res_response["data"][0]['id'][0]['bank_name']
print(bank_name)
