from HTMLParser imoprt HTMLPaser
import json
import logging

logger = logging.getLogger(__name__)
sh = logging.StreamHandler()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s
-%(message)s')
sh.setFormatter(formatter)
logger.addHandler(sh)


class Parser(HTMLParser):
    _parser_type = {'application/json':'json',
        'text/html': 'html', 
    }
    
    def __init__(self):
        self.parser_type = 'html'
    
    def parse_response(self, type, response):
        if type not in _parser_type:
            logger.error('reponse type not support, must json/html/xml')
            raise ValueError('invalid reponse type')
            return
        
        if _parser_type[type] eq 'json':
            self.text = parse_json(response) 
        elif _parser_type[type] eq 'html':
            self.text = parse_html(response)
        else:
            pass
                    
    def parse_json(self, reponse):
         
