import google.auth.transport.requests
import requests

class Client(object):
    """
    Google Cloud Print API Client
    """

    def __init__(self, credentials):
        self.session = requests.Session()
        self.authorize(credentials)


    def authorize(self, credentials):
        if credentials.token is None:
            request = google.auth.transport.requests.Request()
            credentials.refresh(request)

        self.token = credentials.token
        self.session.headers.update({
            'Authorization': 'Bearer {}'.format(self.token) 
        })

    def query(self, method, endpoint, **kwargs):
        from urllib.parse import urljoin

        BASE = "https://www.google.com/cloudprint/"
        url = urljoin(BASE, endpoint)

        files = None
        if "files" in kwargs:
            files = kwargs.pop("files")

        if method == 'get':
            r = self.session.get(url, params=kwargs)
        elif method == 'post':
            r = self.session.post(url, data=kwargs, files=files)
        else:
            # FIXME
            raise Exception("invalid method: {}".format(method))

        if r.ok:
            return r.json()
        return r

    def list_printers(self, q=None):
        r = self.query("get", "search", q=q)
        return r["printers"]

    def print_pdf(self, printer, pdf_name, title=None):
        import uuid

        if title is None:
            title = pdf_name

        with open(pdf_name, "rb") as f:
            content = f.read()

        files = {"content": [pdf_name, content]}

        r = self.query('post', 'submit',
                files=files,
                printerid=printer['id'],
                title=title,
                ticket='{"version": "1", "print": {}}',
                content=content,
                contentType='application/pdf')
        return r

