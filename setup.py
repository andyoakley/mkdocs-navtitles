
from distutils.core import setup

setup(
    name='mkdocs-navtitles',
    version='0.1.0',
    author='Andy Oakley',
    author_email='ao@ao.vc',
    packages=['mkdocs_navtitles'],
    license='LICENSE.txt',
    description='Mkdocs plugin that loads all page titles from source.',
    install_requires=[
    ],

    entry_points={
        'mkdocs.plugins': [
            'navtitles = mkdocs_navtitles:NavTitleLoader',
        ]
    }
)

