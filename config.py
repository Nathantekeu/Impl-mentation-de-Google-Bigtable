import os
from google.cloud import bigtable

PROJECT_ID  = "ventespleindefoin"
INSTANCE_ID = "ventespleindefoin-prod"

# Chaque dev utilise sa propre clé
# Remplace "dev1" par "dev2", "dev3" ou "dev4" selon ton numéro
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, "credentials/dev1-bigtable.json")

def get_instance():
    """Connecte-toi à l'instance BigTable avec 4 nœuds"""
    client = bigtable.Client(project=PROJECT_ID, admin=True)
    return client.instance(INSTANCE_ID)