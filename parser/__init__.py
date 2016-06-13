from HTMLParser imoprt HTMLPaser

class Parser(HTMLParser):
    _parser_type = ['json', 'html', 'xml']
    def __init__(self):
        self.parser_type = 'html'
