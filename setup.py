from setuptools import setup, find_packages

setup(
    name='spotipymodel',
    version='0.0.1',
    description='simple model over the Spotipy web client',
    author='Seth White',
    url='https://github.com/sethwhite23/SpotipyModel',
    install_requires=[
        'spotipy>=2.4.4'
    ],
    packages=find_packages()
)
