from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def home():
    return "Hello, Flask!"

# Run the server
if __name__ == '__main__':
    app.run(debug=True)