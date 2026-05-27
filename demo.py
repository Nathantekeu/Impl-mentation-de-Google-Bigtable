#!/usr/bin/env python3
"""
Script de démonstration complète du projet VentesPleinDeFoin
"""
import subprocess
import sys

def run_demo():
    print("\n" + "="*60)
    print("🎬 DÉMONSTRATION — VentesPleinDeFoin avec Bigtable")
    print("="*60 + "\n")
    
    scripts = [
        ("lire_client.py", "📌 LIRE UN CLIENT"),
        ("lire_commande.py", "📦 LIRE UNE COMMANDE"),
        ("lire_catalogue.py", "🛒 LIRE LE CATALOGUE"),
        ("lire_livraison.py", "🚚 LIRE UNE LIVRAISON"),
        ("modifier_stock_article.py", "✏️  MODIFIER LE STOCK"),
        ("supprimer_commande.py", "🗑️  SUPPRIMER UNE COMMANDE"),
        ("total_par_client.py", "📊 TOTAL PAR CLIENT (GROUP BY)"),
        ("commandes_avec_clients_details.py", "🔗 JOINTURE COMPLÈTE"),
    ]
    
    for script, title in scripts:
        print(f"\n{title}")
        print("-" * 60)
        try:
            subprocess.run([sys.executable, script], check=True)
        except subprocess.CalledProcessError:
            print(f"⚠️ Erreur dans {script}")
        input("\n[Appuie sur Entrée pour continuer...]\n")
    
    print("\n" + "="*60)
    print("✅ FIN DE LA DÉMO")
    print("="*60 + "\n")

if __name__ == "__main__":
    run_demo()