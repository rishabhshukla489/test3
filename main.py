from flask import Flask, request,render_template
import pysftp

app = Flask(__name__)

@app.route('/get_file', methods=['GET'])
def get_file():
    # Parse JSON payload
    sftp_host = request.args.get('host')
    sftp_user = request.args.get('user')
    sftp_pass = request.args.get('password')
    sftp_remote_path = request.args.get('remote_path')

    # Connect to SFTP server
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  
    with pysftp.Connection(host=sftp_host, username=sftp_user, password=sftp_pass,cnopts=cnopts) as sftp:
        # Get file content
        with sftp.open(sftp_remote_path) as file:
            file_content = file.read()

    return file_content
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
