from flask import Flask, request
from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)
import os, uuid
connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
q_name = "highpriority"
queue_client = QueueClient.from_connection_string(connect_str, q_name)

message = u"Hello World"
print("Adding message: " + message)
queue_client.send_message(message)


app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>High Priority</h1>"
    
if __name__ == '__main__':
    app.run()