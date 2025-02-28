from flask import Flask, send_from_directory
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    logger.debug("Serving index.html")  # Debug log
    try:
        return send_from_directory('www', 'index.html')
    except Exception as e:
        logger.error(f"Error serving index.html: {str(e)}")
        return f"Error: {str(e)}", 500

@app.route('/<path:path>')
def static_files(path):
    logger.debug(f"Serving static file: {path}")  # Debug log
    try:
        return send_from_directory('www', path)
    except Exception as e:
        logger.error(f"Error serving {path}: {str(e)}")
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    # Added debug logging
    logger.info("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)