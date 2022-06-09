from flask import Flask, request
from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)
import os, uuid
app = Flask(__name__)

connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
q_name = "highpriority"
queue_client = QueueClient.from_connection_string(connect_str, q_name)

@app.route('/home')
def home():
    message = "Pyton API testing 001"
    queue_client.send_message(message)

    return "<h1>Success</h1>"

if __name__ == '__main__':
    app.run()