class Alert(object):

    def __init__(self, message: str, fields: dict = None):
        if fields is None:
            fields = {}

        self.fields = fields
        self.message = message
