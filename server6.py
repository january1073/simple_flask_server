# Flask server with custom error handler

from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def api_not_found(error):
    # Custom error handler for 404 Not Found errors
    return {"message": "API not found"}, 404

# Run the server
if __name__ == '__main__':
    app.run(debug=True)