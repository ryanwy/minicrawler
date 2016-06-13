import random
import requests

from . import SettingsProxy

class Proxy(object):

    DEFAULT_CODE = 100

    def __init__(self):
        self.settings = SettingsProxy.load_object()
        self.code = self.DEFAULT_CODE
        self.proxy_enable = self.settings['PROXY_ENABLE']
        if self.proxy_enable:
            self.proxy_method = self.settings['PROXY_METHODS'][self.code]
            self.proxy_host = self.settings['PROXY_HOSTS'][self.code]
            self.proxy_url = self.settings['PROXY_URLS'][self.code]
            self.proxy_refer = self.settings['PROXY_REFER'][self.code]
            self.proxy_x_request = self.settings['PEOXY_X_REQUEST'][self.code]
            self.proxy_cookie_enable = self.settings['PROXY_COOKIE_ENABLE']
            if self.proxy_cookie_enable:
                self.proxy_cookie = self.settings['PROXY_COOKIES'][self.code]
            else:
                self.proxy_cookie = None
            self.proxy_data_usrpsw_enable = self.settings['DATA_USER_PSW_ENABLE']
            if self.proxy_data_usrpsw_enable:
                self.proxy_data_usrpsw = self.settings['PROXY_DATA_USER_PSW'][self.code]
            else:
                self.proxy_data_usrpsw = None
            self.proxy_server = self.settings['PROXY_SERVER']
            self.proxy_agent = random.choice(self.settings['PROXY_USER_AGENT'])
            self.proxy_payload = self.settings['PROXY_PAYLOAD'][self.code]            
            self.proxy_delay = self.settings['PROXY_CHECK_TIMEOUT']

    def get_proxy(self):
        self.headers = {
            'Host' : self.proxy_host,
            'Referer' : self.proxy_refer,
            'X-Requested-With' : self.proxy_x_request,
            'User-Agent' : self.proxy_agent,
            'Cookie' : self.proxy_cookie,
        }
        import pdb
        pdb.set_trace()
        if self.proxy_method == 'session-post':
            self.session = requests.Session()
            self.session.headers.update(self.headers)    
            self.response = self.session.post(self.proxy_url, data = self.proxy_payload)
        elif self.proxy_method == 'get':
            pass
        elif self.proxy_method == 'post':
            pass
        else:
            pass
        
        if self.response.status_code == 200:
            self.res_content_type = self.response.headers.get('content-type')
                    
