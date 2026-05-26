import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import get_instance

def create_tables():
    instance = get_instance()
    
    tables = {
        "clients": ["info"],
        "articles": ["info", "stock"],
        "commandes": ["info", "lignes"],
        "livraisons": ["info", "detail"]
    }
    
    print("Création des tables...")
    
    for table_name, families in tables.items():
        table = instance.table(table_name)
        
        if table.exists():
            print(f"  ⚠️  Table '{table_name}' existe déjà — ignorée")
            continue
        
        table.create()
        
        for family in families:
            table.column_family(family).create()
        
        print(f"  ✅ Table '{table_name}' créée avec colonnes : {families}")
    
    print("\nToutes les tables sont prêtes !")

if __name__ == "__main__":
    create_tables()