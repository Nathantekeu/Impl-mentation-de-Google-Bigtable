from config import get_instance

def obtenir_client(id_client):
    instance = get_instance()
    table = instance.table("clients")
    
    # Lecture directe via la Row Key
    row = table.read_row(f"client#{id_client}")
    
    if row:
        nom = row.cells['info'][b'nom'][0].value.decode('utf-8')
        tel = row.cells['info'][b'telephone'][0].value.decode('utf-8')
        print(f"=== Infos Client {id_client} ===")
        print(f"Nom : {nom}")
        print(f"Téléphone : {tel}\n")
    else:
        print(f"❌ Le client {id_client} n'existe pas.")

if __name__ == "__main__":
    obtenir_client("10") # Test avec le client 10 (Luc Sansom)