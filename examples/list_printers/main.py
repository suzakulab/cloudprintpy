from google.oauth2 import service_account
import cloudprint
import sys


def main():
    # google api scopes
    scopes = [
        "https://www.googleapis.com/auth/cloudprint",
    ]

    # credential for google service account
    credentials = service_account.Credentials.from_service_account_file("service-account-credential-xxxxxxxxx.json", scopes=scopes)

    # Google Cloud Print Client
    client = cloudprint.Client(credentials)

    # list printers filtered by argv[1] (or list all printers)
    name = sys.argv[1] if len(sys.argv) >= 2 else ''
    for printer in client.list_printers(name):
        print(printer)

if __name__ == '__main__':
    main()
