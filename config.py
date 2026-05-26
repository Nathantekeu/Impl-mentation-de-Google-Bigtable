import os
from google.cloud import bigtable

PROJECT_ID  = "ventespleindefoin"  # ton Project ID GCP
INSTANCE_ID = "ventespleindefoin"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/dev1-bigtable.json"

def get_instance():
    client = bigtable.Client(project=PROJECT_ID, admin=True)
    return client.instance(INSTANCE_ID)