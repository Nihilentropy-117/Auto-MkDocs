import logging
from flask import Flask, send_from_directory, current_app
from urllib.parse import unquote

app = Flask(__name__, static_folder='/app/site')
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@app.route('/<path:path>')
def send_static(path):
    logger.info(f"Entered")
    logger.info(f"Entered send_static with path: {path}")
    decoded_path = unquote(path)

    logger.info(f"Decoded path before: {decoded_path}")

    # Check if the path ends with a '/', and if so, append only 'index.html'
    if decoded_path.endswith('/'):
        decoded_path = decoded_path + 'index.html'

    logger.info(f"Decoded path after: {decoded_path}")
    return send_from_directory('/app/site', decoded_path)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)