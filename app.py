from flask import Flask, request
from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)
import os, uuid
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>We're home<h>"
    
'''
@app.route('/addtoq')
def home():    
    q_name = "highpriority"
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    queue_client = QueueClient.from_connection_string(connect_str, q_name)
    message = "Pyton API testing 001"
    queue_client.send_message(message)
    return message
    '''

if __name__ == '__main__':
    app.run()