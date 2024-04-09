class Document:
    def view(self):
        pass


class RealDocument(Document):
    def __init__(self, content):
        self._content = content

    def view(self):
        print("Document data:", self._content)


class ProxyDocument(Document):
    def __init__(self, document, user_role):
        self._document = document
        self._user_role = user_role

    def view(self):
        if self._user_role == "admin":
            self._document.view()
        else:
            print("You don't have permission to read the document.")


def main():
    real_document = RealDocument("Secret data.")

    admin_document_proxy = ProxyDocument(real_document, "admin")
    admin_document_proxy.view()

    user_document_proxy = ProxyDocument(real_document, "user")
    user_document_proxy.view()


if __name__ == "__main__":
    main()
