from setuptools import setup

setup(
    name = 'minicrawler'
    version = '0.1.0'
    description = 'A light weighed web crawler',
    maintainer = 'ryanwy',
    maintainer_email = 'wangyan_ryan@163.com',
    license = 'LGPL',
    install_requires = [
        'requests>=2.10.0',
    ],
)
