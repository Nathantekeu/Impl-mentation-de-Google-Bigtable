from config import get_instance

def total_par_client():
    """
    SELECT noClient, COUNT(*), SUM(prix*quantite) 
    FROM commandes GROUP BY noClient
    """
    instance = get_instance()
    table_cmds = instance.table("commandes")
    table_articles = instance.table("articles")
    
    clients_data = {}
    
    # Lire toutes les commandes
    rows = table_cmds.read_rows()
    for row in rows:
        id_client = row.cells['info'][b'client'][0].value.decode('utf-8')
        
        if id_client not in clients_data:
            clients_data[id_client] = {"count": 0, "total": 0}
        
        clients_data[id_client]["count"] += 1
        
        # Calculer le total de cette commande
        for family_name, columns in row.cells.items():
            if family_name in ['lignes', b'lignes']:
                for col_qualifier, cells in columns.items():
                    col_str = col_qualifier.decode('utf-8')
                    art_id = col_str.replace('art', '')
                    quantite = int(cells[0].value.decode('utf-8'))
                    
                    # Récupérer le prix de l'article
                    row_article = table_articles.read_row(f"article#{art_id}")
                    if row_article:
                        prix = float(row_article.cells['info'][b'prix'][0].value.decode('utf-8'))
                        clients_data[id_client]["total"] += prix * quantite
    
    print("\n=== TOTAL PAR CLIENT (GROUP BY) ===\n")
    print("Client ID | Nombre de cmds | Total ($)")
    print("-" * 45)
    for client_id in sorted(clients_data.keys()):
        data = clients_data[client_id]
        print(f"{client_id.ljust(9)} | {str(data['count']).ljust(14)} | {data['total']:.2f}$")

if __name__ == "__main__":
    total_par_client()