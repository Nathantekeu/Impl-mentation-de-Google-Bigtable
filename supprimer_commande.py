from config import get_instance

def supprimer_commande(id_commande):
    """
    DELETE FROM commandes WHERE noCommande = ?
    """
    instance = get_instance()
    table = instance.table("commandes")
    
    row_key = f"commande#{id_commande.zfill(4)}"
    row = table.direct_row(row_key)
    row.delete()
    
    print(f"✅ Commande {id_commande} supprimée avec succès")

if __name__ == "__main__":
    supprimer_commande("8")  # Supprime la commande 8