from config import get_instance

def detailler_commande(id_cmd):
    instance = get_instance()
    table_cmd = instance.table("commandes")
    table_clients = instance.table("clients")
    table_articles = instance.table("articles")
    
    # 1. Lire la commande spécifique via sa Row Key (ex: commande#0001)
    row_key_cmd = f"commande#{id_cmd.zfill(4)}"
    row_cmd = table_cmd.read_row(row_key_cmd)
    if not row_cmd:
        print(f"❌ La commande {id_cmd} est introuvable.")
        return
        
    # Extraction sécurisée des infos de base
    date = row_cmd.cells['info'][b'date'][0].value.decode('utf-8')
    id_client = row_cmd.cells['info'][b'client'][0].value.decode('utf-8')
    
    # Récupérer le nom du client
    row_client = table_clients.read_row(f"client#{id_client}")
    nom_client = row_client.cells['info'][b'nom'][0].value.decode('utf-8') if row_client else "Inconnu"
    
    print(f"=== DETAIL DE LA COMMANDE N° {id_cmd.zfill(4)} ===")
    print(f"Date    : {date}")
    print(f"Client  : {nom_client} (ID: {id_client})")
    print("Articles commandés :")
    
    # On inspecte toutes les familles disponibles dans l'objet retourné
    for family_name, columns in row_cmd.cells.items():
        # On vérifie si la famille est 'lignes' (que ce soit en string ou en bytes)
        if family_name in ['lignes', b'lignes']:
            for col_qualifier, cells in columns.items():
                # col_qualifier est en bytes (ex: b'art10'), on le décode
                col_str = col_qualifier.decode('utf-8')
                art_id = col_str.replace('art', '')
                quantite = cells[0].value.decode('utf-8')
                
                # Récupération de la description de l'article
                row_article = table_articles.read_row(f"article#{art_id}")
                desc_article = "Article inconnu"
                if row_article:
                    # Sécurité si Claude l'a appelé 'description' ou 'desc'
                    info_family = row_article.cells['info']
                    if b'description' in info_family:
                        desc_article = info_family[b'description'][0].value.decode('utf-8')
                    elif b'desc' in info_family:
                        desc_article = info_family[b'desc'][0].value.decode('utf-8')
                
                print(f"  - [ID {art_id}] {desc_article.ljust(15)} -> Quantité commandée : {quantite}")

if __name__ == "__main__":
    detailler_commande("1")