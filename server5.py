# Flask server parsing JSON from request body

from flask import Flask, request
app = Flask(__name__)

data = [{"id":"3b58aade-8415-49dd-88db-8d7bce14932a","first_name":"Baxy","last_name":"Escalera","email":"bescalera0@wikispaces.com","ip_address":"107.160.207.177"},
{"id":"d64efd92-ca8e-40da-b234-47e6403eb167","first_name":"Marigold","last_name":"Tillyer","email":"mtillyer1@clickbank.net","ip_address":"80.162.216.11"},
{"id":"66c09925-589a-43b6-9a5d-d1601cf53287","first_name":"Ware","last_name":"Jenson","email":"wjenson2@addthis.com","ip_address":"117.133.217.112"},
{"id":"a3d8adba-4c20-495f-b4c4-f7de8b9cfb15","first_name":"Joline","last_name":"Phette","email":"jphette3@phpbb.com","ip_address":"54.54.173.177"}]

@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
    # code to validate new_person ommited
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"{new_person['id']}"}, 200

# Run the server
if __name__ == '__main__':
    app.run(debug=True)

# Test:
# curl -X POST -i -w '\n' \
#   --url http://localhost:5000/person \
#   --header 'Content-Type: application/json' \
#   --data '{
#         "id": "0z7e61b4-6b27-87ed-00eb-0662ac139993",
#         "first_name": "Peter",
#         "last_name": "Parker",
#         "email": "spidy3@gotham.com",
#         "ip_address": "24.54.173.177"
#     }'