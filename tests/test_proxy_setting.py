"""
test module proxy settings
"""

import sys
import os

PROJECT_NAME = 'minicrawler'

def init_env():
    prj_path = find_prj_path()
    if prj_path not in sys.path:
        sys.path.append(prj_path)

def find_prj_path(path='.'):
    path = os.path.abspath(path)
    prjpath = os.path.join(path, PROJECT_NAME)
    if os.path.exists(prjpath):
        return prjpath
    return find_prj_path(os.path.dirname(path))

def main():
    init_env()
    from proxy import SettingsProxy
    setting = SettingsProxy()
    print setting['PROXY_URLS']
    print setting['PROXY_METHODS'][100]
    print setting['PROXY_USER_AGENT'][1]
    from proxy.get_proxy import Proxy
    proxy = Proxy()
    proxy.get_proxy()

if __name__ == '__main__':
    main()
