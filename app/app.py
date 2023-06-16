import os
from flask import Flask, render_template, request, redirect, send_file
from s3_helper import list_all_files, download, upload

app = Flask(__name__)
UPLOAD_FOLDER = "upload_files"
BUCKET = "cs630-qd-bucket"

@app.route('/')
def start():
    return "Welcome to Server 2!"

@app.route("/home")
def home():
    contents = list_all_files(BUCKET)
    server_name = "Server 2"
    return render_template('s3_storage_dashboard.html', contents= [contents, server_name])

@app.route("/upload", methods=['POST'])
def upload_files():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        upload(f"upload_files/{f.filename}", BUCKET, f.filename)
        return redirect("/home")


@app.route("/download/<filename>", methods=['GET'])
def download_files(filename):
    if request.method == 'GET':
        output = download(filename, BUCKET)
        return send_file(output, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)