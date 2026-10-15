from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My QR Print</title>
    </head>
    <body>
        <h1>QR Print System</h1>
        <p>हमारा अपना QR Print System शुरू हो गया है!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)