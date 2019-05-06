"""Setup and install as a package."""
import os

from setuptools import setup, find_packages


def read(filename):
    """Read file contents."""
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), filename))
    with open(path, 'rb') as f:
        return f.read().decode('utf-8')


requirements = read('requirements.txt').split()

readme = read('README.md')

setup(
    name='dtp-cli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        requirements,
    ],
    entry_points='''
        [console_scripts]
        dtp-cli=client.main:get_time
    ''',
)
