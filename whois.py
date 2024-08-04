import whois
import re
import os


def validate_domain(domain):
    # Utilisation d'une expression régulière simple pour valider le format du domaine
    pattern = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, domain) is not None


def format_date(date):
    if isinstance(date, list):
        date = date[0]
    return date.strftime('%Y-%m-%d') if date else 'N/A'


def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        output = {
            'Nom du domaine': domain_info.domain_name,
            'Registrar': domain_info.registrar,
            'Date de création': format_date(domain_info.creation_date),
            'Date d\'expiration': format_date(domain_info.expiration_date),
            'Serveurs DNS': ', '.join(domain_info.name_servers) if domain_info.name_servers else 'N/A',
            'Status': ', '.join(domain_info.status) if domain_info.status else 'N/A',
            'Email de contact': ', '.join(domain_info.emails) if domain_info.emails else 'N/A',
            'Organisation': domain_info.org if domain_info.org else 'N/A'
        }
        return output
    except Exception as e:
        return {'Erreur': f'Une erreur est survenue lors de la recherche WHOIS: {e}'}


def display_info(info):
    for key, value in info.items():
        print(f"{key}: {value}")


def save_info_to_file(domain, info):
    with open(f"{domain}_whois.txt", "w") as file:
        for key, value in info.items():
            file.write(f"{key}: {value}\n")


def main():
    while True:
        # Demander à l'utilisateur de saisir un ou plusieurs domaines
        domains_input = input("Entrez le(s) domaine(s) séparés par une virgule (ex. example.com, test.org): ")
        domains = [domain.strip() for domain in domains_input.split(',')]

        for domain in domains:
            if not validate_domain(domain):
                print(f"Le domaine '{domain}' n'est pas valide.")
                continue

            print(f"\nRecherche WHOIS pour le domaine {domain}...")
            info = get_domain_info(domain)

            display_info(info)

            # Demander à l'utilisateur s'il souhaite sauvegarder les résultats
            save_option = input(
                f"\nSouhaitez-vous sauvegarder les informations dans un fichier pour '{domain}' ? (o/n): ").strip().lower()
            if save_option == 'o':
                save_info_to_file(domain, info)
                print(f"Les informations ont été enregistrées dans le fichier '{domain}_whois.txt'.")

        # Vérifier si l'utilisateur souhaite effectuer une autre recherche
        another_search = input("\nSouhaitez-vous effectuer une autre recherche ? (o/n): ").strip().lower()
        if another_search != 'o':
            print("Merci d'avoir utilisé le service WHOIS Lookup. À bientôt !")
            break


if __name__ == "__main__":
    main()
