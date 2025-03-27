# Flask server processing input arguments

from flask import Flask, request
app = Flask(__name__)

# The data is generated with Mockaroo (https://www.mockaroo.com/)
data = [{"id":1,"first_name":"Baxy","last_name":"Escalera","email":"bescalera0@wikispaces.com","ip_address":"107.160.207.177"},
{"id":2,"first_name":"Marigold","last_name":"Tillyer","email":"mtillyer1@clickbank.net","ip_address":"80.162.216.11"},
{"id":3,"first_name":"Ware","last_name":"Jenson","email":"wjenson2@addthis.com","ip_address":"117.133.217.112"},
{"id":4,"first_name":"Joline","last_name":"Phette","email":"jphette3@phpbb.com","ip_address":"54.54.173.177"}]

# Create an end point that returns the person’s data to the client in JSON format
@app.route("/name_search")
def name_search():
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')
    # Check if the query parameter 'q' is missing
    if not query:
        # Return a JSON response with a message indicating 'q' is missing and a 422 Unprocessable Entity status code
        return {"message": "Query parameter 'q' is missing"}, 422
    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            # If a match is found, return the person as a JSON response with a 200 OK status code
            return person
    # If no match is found, return a JSON response with a message indicating the person was not found and a 404 Not Found status code
    return {"message": "Person not found"}, 404

# Run the server
if __name__ == '__main__':
    app.run(debug=True)

# Test: curl -X GET -i -w '\n' "localhost:5000/name_search?q=Joline"