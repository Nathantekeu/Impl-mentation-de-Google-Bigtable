from config import get_instance

def lister_catalogue():
    instance = get_instance()
    table = instance.table("articles")
    
    print("=== CATALOGUE DES ARTICLES ===")
    # On scanne toute la table articles (équivalent d'un SELECT * sans clause)
    rows = table.read_rows()
    
    for row in rows:
        art_id = row.row_key.decode('utf-8').replace('article#', '')
        desc = row.cells['info'][b'description'][0].value.decode('utf-8')
        prix = row.cells['info'][b'prix'][0].value.decode('utf-8')
        qty = row.cells['stock'][b'quantite'][0].value.decode('utf-8')
        print(f"ID {art_id.zfill(2)} | {desc.ljust(18)} | Prix: {prix}$ | Stock: {qty}")

if __name__ == "__main__":
    lister_catalogue()