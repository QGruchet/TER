import argparse

from src.database.creation_bd import connexion, remplissage
from src.scrapping import scrap_article_court, scrap_article_long


def main(user, pwd, host, port, db):
    print("Scrapping information article court")
    articles_court = scrap_article_court()
    print("Scrapping information article long")
    articles_long = scrap_article_long()
    print("Connexion")
    engines = connexion(user, pwd, host, port, db)
    print("Remplir article court")
    remplissage(engines, articles_court)
    print("Remplir article long")
    remplissage(engines, articles_long)
    print("Fin")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pipeline d\'intégration de données du site les surligneurs')
    parser.add_argument("--user", dest="user", help="Pseudonyme utilisateur")
    parser.add_argument("--pwd", dest="pwd", help="Mot de passe utilisateur")
    parser.add_argument("--host", dest="host", help="Adresse de la base de donnée cible")
    parser.add_argument("--port", dest="port", help="Port de la machine cible")
    parser.add_argument("--db", dest="db", help="Base de donnée cible")
    args = parser.parse_args()

    main(args.user, args.pwd, args.host, args.port, args.db)
