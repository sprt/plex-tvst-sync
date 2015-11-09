import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

# TODO: setup crontab entry on install

setup(
    name='plex-tvst-sync',
    version='0.1.0',
    author='sprt',
    author_email='hellosprt@gmail.com',
    url='https://github.com/sprt/plex-tvst-sync',
    install_requires=[
        'PlexAPI==1.1.0',
        'requests==2.8.1',
    ],
    entry_points={'console_scripts': ['plex-tvst-sync = scrobbler:main']},
)
