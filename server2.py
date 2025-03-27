# Flask server with set response status code

from flask import Flask, make_response

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "Hello, Flask!"

# Define a route for the "/no_content" URL
@app.route("/no_content")
def no_content():
    # Create a dictionary with a message and return it with a 204 No Content status code
    return ({"message": "No content found"}, 204)

# Define a route for the "/exp" URL
@app.route("/exp")
def index_explicit():
    # Create a response object with the message "Hello, Flask!"
    resp = make_response({"message": "Hello, Flask!"})
    # Set the status code of the response to 200
    resp.status_code = 200
    # Return the response object
    return resp

# Run the server
if __name__ == '__main__':
    app.run(debug=True)