# Flask server with dynamic URLs (GET /count, GET /person/id, and DELETE /person/id endpoints)

from flask import Flask, request
app = Flask(__name__)

data = [{"id":"3b58aade-8415-49dd-88db-8d7bce14932a","first_name":"Baxy","last_name":"Escalera","email":"bescalera0@wikispaces.com","ip_address":"107.160.207.177"},
{"id":"d64efd92-ca8e-40da-b234-47e6403eb167","first_name":"Marigold","last_name":"Tillyer","email":"mtillyer1@clickbank.net","ip_address":"80.162.216.11"},
{"id":"66c09925-589a-43b6-9a5d-d1601cf53287","first_name":"Ware","last_name":"Jenson","email":"wjenson2@addthis.com","ip_address":"117.133.217.112"},
{"id":"a3d8adba-4c20-495f-b4c4-f7de8b9cfb15","first_name":"Joline","last_name":"Phette","email":"jphette3@phpbb.com","ip_address":"54.54.173.177"}]

# Create GET /count endpoint
@app.route("/count")
def count():
    try:
        # Attempt to return a JSON response with the count of items in 'data'
        return {"data count": len(data)}, 200
    except NameError:
        # If 'data' is not defined and raises a NameError
        return {"message": "data not defined"}, 500

# Create GET /person/id endpoint
@app.route("/person/<var_name>")
def find_by_uuid(var_name):
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field of the person matches the 'var_name' parameter
        if person["id"] == str(var_name):
            # Return the person as a JSON response if a match is found
            return person

    # Return a JSON response with a message and a 404 Not Found status code if no matching person is found
    return {"message": "Person not found"}, 404

# Create DELETE /person/id endpoint
@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    # Iterate through the 'data' list to search for a person with a matching ID
    for person in data:
        # Check if the 'id' field of the person matches the 'id' parameter
        if person["id"] == str(id):
            # Remove the person from the 'data' list
            data.remove(person)
            # Return a JSON response with a message confirming deletion and a 200 OK status code
            return {"message": f"Person with ID {id} deleted"}, 200
    # If no matching person is found, return a JSON response with a message and a 404 Not Found status code
    return {"message": "person not found"}, 404

# Run the server
if __name__ == '__main__':
    app.run(debug=True)

# Test GET /count endpoint: curl -X GET -i -w '\n' "localhost:5000/count"
# Test GET /person/id endpoint: curl -X GET -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
# Test DELETE /person/id endpoint:
# - Delete: curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
# - Check: