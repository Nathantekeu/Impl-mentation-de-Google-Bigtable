from config import get_instance

def mettre_a_jour_stock(id_article, nouvelle_quantite):
    """
    UPDATE articles SET quantiteEnStock = ? WHERE noArticle = ?
    """
    instance = get_instance()
    table = instance.table("articles")
    
    row = table.direct_row(f"article#{id_article}")
    row.set_cell("stock", "quantite", str(nouvelle_quantite))
    row.commit()
    
    print(f"✅ Article {id_article} : stock mis à jour à {nouvelle_quantite} unités")

if __name__ == "__main__":
    mettre_a_jour_stock("10", "5")  # Cèdre : 10 → 5 unités