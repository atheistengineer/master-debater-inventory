import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

from flask import Flask
app = Flask(__name__)

# https://docs.microsoft.com/en-us/azure/app-service/containers/how-to-configure-python

@app.route("/")
def hello():
    return "Hello Other World!"