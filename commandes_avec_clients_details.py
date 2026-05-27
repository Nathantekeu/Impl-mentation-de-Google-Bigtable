from config import get_instance

def commandes_avec_clients_et_totaux():
    """
    SELECT c.noCommande, c.dateCommande, cl.nomClient, 
           COUNT(*) as nbArticles, SUM(prix*quantite) as total
    FROM commandes c
    JOIN clients cl ON c.noClient = cl.noClient
    JOIN articles a ON lc.noArticle = a.noArticle
    GROUP BY c.noCommande
    """
    instance = get_instance()
    table_cmds = instance.table("commandes")
    table_clients = instance.table("clients")
    table_articles = instance.table("articles")
    
    print("\n=== COMMANDES AVEC DÉTAILS (JOINTURE) ===\n")
    print("Cmd# | Date       | Client              | Nb articles | Total ($)")
    print("-" * 75)
    
    rows = table_cmds.read_rows()
    for row in rows:
        id_cmd = row.row_key.decode('utf-8').replace('commande#', '')
        date = row.cells['info'][b'date'][0].value.decode('utf-8')
        id_client = row.cells['info'][b'client'][0].value.decode('utf-8')
        
        # Récupérer le client
        row_client = table_clients.read_row(f"client#{id_client}")
        nom_client = row_client.cells['info'][b'nom'][0].value.decode('utf-8') if row_client else "Inconnu"
        
        # Compter articles et calculer total
        nb_articles = 0
        total = 0
        
        for family_name, columns in row.cells.items():
            if family_name in ['lignes', b'lignes']:
                for col_qualifier, cells in columns.items():
                    col_str = col_qualifier.decode('utf-8')
                    art_id = col_str.replace('art', '')
                    quantite = int(cells[0].value.decode('utf-8'))
                    nb_articles += 1
                    
                    row_article = table_articles.read_row(f"article#{art_id}")
                    if row_article:
                        prix = float(row_article.cells['info'][b'prix'][0].value.decode('utf-8'))
                        total += prix * quantite
        
        print(f"{id_cmd.ljust(4)} | {date} | {nom_client.ljust(19)} | {str(nb_articles).ljust(11)} | {total:.2f}$")

if __name__ == "__main__":
    commandes_avec_clients_et_totaux()