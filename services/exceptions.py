class InputError(Exception):
    def __init__(self, row):
        self.message = "Parsing error: {row}"


class DataError(Exception):
    def __init__(self, value):
        self.message = "Data type error: {value}"
