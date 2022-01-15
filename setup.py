import setuptools

NAME           = 'ytm'
VERSION        = '0.0.1'
DESCRIPTION    = 'Python YouTube Music Web API Client'
AUTHOR         = 'Tom Bulled'
URL            = 'https://github.com/tombulled/python-youtube-music'
PACKAGES       = setuptools.find_packages()
PYTHON_VERSION = '>=3.0.0'

DEPENDENCIES_REQUIRED = \
(
    'requests',
)

DEPENDENCIES_OPTIONAL = \
{
    'dl': \
    (
        'youtube-dl',
        'mutagen',
        'Pillow',
    ),
    'dev': \
    (
        'pytest',
    ),
}

config = dict \
(
   name             = NAME,
   version          = VERSION,
   description      = DESCRIPTION,
   author           = AUTHOR,
   packages         = PACKAGES,
   install_requires = DEPENDENCIES_REQUIRED,
   extras_require   = DEPENDENCIES_OPTIONAL,
   python_requires  = PYTHON_VERSION,
   url              = URL,
)

setuptools.setup(**config)
