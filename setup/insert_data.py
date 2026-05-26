import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_instance

def insert_all():
    instance = get_instance()

    # ── CLIENTS ──────────────────────────────────────────
    table = instance.table("clients")
    clients = [
        ("10", "Luc Sansom",       "(999)999-9999"),
        ("20", "Dollard Tremblay", "(888)888-8888"),
        ("30", "Lin Be",           "(777)777-7777"),
        ("40", "Jean Leconte",     "(666)666-6666"),
        ("50", "Hafed Alaoui",     "(555)555-5555"),
        ("60", "Marie Leconte",    "(666)666-6666"),
        ("70", "Simon Lecoq",      "(444)444-4419"),
        ("80", "Dollard Tremblay", "(333)333-3333"),
    ]
    for no, nom, tel in clients:
        row = table.direct_row(f"client#{no}")
        row.set_cell("info", "nom",       nom)
        row.set_cell("info", "telephone", tel)
        row.commit()
    print("✅ Clients insérés")

    # ── ARTICLES ─────────────────────────────────────────
    table = instance.table("articles")
    articles = [
        ("10", "Cedre en boule",   "10.99"),
        ("20", "Sapin",            "12.99"),
        ("40", "Epinette bleue",   "25.99"),
        ("50", "Chene",            "22.99"),
        ("60", "Erable argente",   "15.99"),
        ("70", "Herbe a puce",     "10.99"),
        ("80", "Poirier",          "26.99"),
        ("81", "Catalpa",          "25.99"),
        ("90", "Pommier",          "25.99"),
        ("95", "Genevrier",        "15.99"),
    ]
    for no, desc, prix in articles:
        row = table.direct_row(f"article#{no}")
        row.set_cell("info",  "description", desc)
        row.set_cell("info",  "prix",         prix)
        row.set_cell("stock", "quantite",     "10")
        row.commit()
    print("✅ Articles insérés")

    # ── COMMANDES ────────────────────────────────────────
    table = instance.table("commandes")
    commandes = [
        ("1", "01/06/2000", "10", {"10":"10", "70":"5",  "90":"1"}),
        ("2", "02/06/2000", "20", {"40":"2",  "95":"3"}),
        ("3", "02/06/2000", "10", {"20":"1"}),
        ("4", "05/07/2000", "10", {"40":"1",  "50":"1"}),
        ("5", "09/07/2000", "30", {"70":"3",  "10":"5",  "20":"5"}),
        ("6", "09/07/2000", "20", {"10":"5",  "40":"1"}),
        ("7", "15/07/2000", "40", {"50":"1"}),
        ("8", "15/07/2000", "40", {"20":"3"}),
    ]
    for no, date, client, lignes in commandes:
        row = table.direct_row(f"commande#{no.zfill(4)}")
        row.set_cell("info", "date",   date)
        row.set_cell("info", "client", client)
        for art, qty in lignes.items():
            row.set_cell("lignes", f"art{art}", qty)
        row.commit()
    print("✅ Commandes insérées")

    # ── LIVRAISONS ───────────────────────────────────────
    table = instance.table("livraisons")
    livraisons = [
        ("100", "03/06/2000", [("1","10","7"), ("1","70","5"), ("3","20","1")]),
        ("101", "04/06/2000", [("1","10","3")]),
        ("102", "04/06/2000", [("2","40","2"), ("2","95","1")]),
        ("103", "05/06/2000", [("1","90","1")]),
        ("104", "07/07/2000", [("4","40","1")]),
        ("105", "08/07/2000", [("5","70","2")]),
    ]
    for no, date, details in livraisons:
        row = table.direct_row(f"livraison#{no}")
        row.set_cell("info", "date", date)
        for cmd, art, qty in details:
            row.set_cell("detail", f"cmd{cmd}_art{art}", qty)
        row.commit()
    print("✅ Livraisons insérées")

    print("\n🎉 Toutes les données sont insérées !")

if __name__ == "__main__":
    insert_all()