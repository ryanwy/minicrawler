import os
import sys
import logging

from importlib import import_module
from . import proxy_template

__all__ = ["SettingsProxy"]

logger = logging.getLogger(__name__)
sh = logging.StreamHandler()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
sh.setFormatter(formatter)
logger.addHandler(sh)


SETTING_PROXY_NAME = 'proxy_template'
PROJECT_NAME = 'minicrawler'


class SettingsProxy(object):
    """
    get proxy template settings

    """

    def __init__(self):
        self.attributes = {}
        self.name = SETTING_PROXY_NAME
        self.init_env()
        self.setmodule(SETTING_PROXY_NAME)
    
    @classmethod
    def load_object(cls):
        settings = cls()
        return settings

    def __getitem__(self, opt_name):
        value = None
        if opt_name in self.attributes:
            value = self.attributes[opt_name]
        return value

    def setmodule(self, module):
        if isinstance(module, basestring):
            module = import_module(module)
            logger.info("load module: %(module)s", {'module':module})
        for key in dir(module):
            if key.isupper():
                self.set_attr(key, getattr(module, key))
    
    def set_attr(self, name, value):
        if name not in self.attributes:
            self.attributes[name] = value

    def init_env(self):
        prj_path = self.find_prj_path()
        if prj_path not in sys.path:
            sys.path.append(prj_path)

        file_found_flag = False
        for dirs in os.walk(prj_path):
            for i in dirs[1]:            
                file_dir = os.path.join(dirs[0], i) + '/' + SETTING_PROXY_NAME + '.py'
                if os.path.isfile(file_dir) and os.path.join(dirs[0], i) not in sys.path:
                    sys.path.append(os.path.join(dirs[0], i))
                    file_found_flag = True
                    break
            if file_found_flag:
                break

    def find_prj_path(self, path='.'):
        path = os.path.abspath(path)
        prjpath = os.path.join(path, PROJECT_NAME)
        if os.path.exists(prjpath):
            return prjpath
        return self.find_prj_path(os.path.dirname(path))


