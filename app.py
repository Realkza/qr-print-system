from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024

UPLOAD_FOLDER = "/tmp/qrprint_uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="hi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>QR Print System</title>
        <style>
            body { font-family: Arial; max-width: 520px; margin: 40px auto; padding: 20px; }
            h1 { color: #1769aa; }
            form { border: 1px solid #ccc; padding: 20px; border-radius: 10px; }
            input, button { margin-top: 15px; width: 100%; padding: 12px; box-sizing: border-box; }
            button { background: #1769aa; color: white; border: 0; border-radius: 6px; }
        </style>
    </head>
    <body>
        <h1>QR Print System</h1>
        <p>PDF या JPG फाइल यहाँ अपलोड करें।</p>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="document" accept=".pdf,.jpg,.jpeg,.png" required>
            <button type="submit">फाइल अपलोड करें</button>
        </form>
        <p>अधिकतम फाइल आकार: 20 MB</p>
    </body>
    </html>
    """

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("document")

    if not file or not file.filename:
        return "कृपया फाइल चुनें।", 400

    filename = secure_filename(file.filename)
    if not filename.lower().endswith((".pdf", ".jpg", ".jpeg", ".png")):
        return "केवल PDF, JPG या PNG फाइल स्वीकार है।", 400

    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)

    return """
    <h2>फाइल अपलोड हो गई!</h2>
    <p>यह अभी केवल ऑनलाइन परीक्षण है। फाइल अपने-आप Epson प्रिंटर पर प्रिंट नहीं होगी।</p>
    <a href="/">वापस जाएँ</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
