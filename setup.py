from distutils.core import setup
from setuptools import find_packages

setup(
    name='kilnapi',
    version='0.2.9',
    author='Aaron McSorley',
    author_email='a@aaronmcsorley.com',
    scripts=['bin/kilnapi'],
    url='https://github.com/amcsorley/kilnapi',
    license='GPLv2',
    description='Kiln controller API',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['tornado', 'argparse',],
    data_files = [ ('/etc/init.d',['kilnapi/init-script/kilnapi']),
                   ('/etc/kilnapi',['kilnapi/config/kilnapi.conf']),
                   ('/etc/pki/kilnapi',['kilnapi/certs/key.pem']),
                   ('/etc/pki/kilnapi',['kilnapi/certs/cert.pem']),
                   ('/etc/pki/kilnapi',['kilnapi/certs/openssl.cnf']),
    ],
)
