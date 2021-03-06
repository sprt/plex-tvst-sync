try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='plex-tvst-sync',
    version='1.0b3',
    author='sprt',
    author_email='hellosprt@gmail.com',
    url='https://github.com/sprt/plex-tvst-sync',
    keywords='plex tvshowtime scrobbler sync',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2 :: Only',
    ],
    py_modules=['scrobbler'],
    setup_requires=[
        'python-crontab==1.9.3',
    ],
    install_requires=[
        'appdirs==1.4.0',
        'PlexAPI==1.1.0',
        'python-crontab==1.9.3',
        'requests==2.8.1',
    ],
    entry_points={'console_scripts': ['plex-tvst-sync = scrobbler:main']},
)
