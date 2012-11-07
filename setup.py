from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES


VERSION = '1.0'


# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


setup(
    name='django-oscar-cielo',
    version=VERSION,
    description="Cielo (brazilian payment gateway) module for django-oscar",
    long_description="",
    author="Caio Ariede",
    author_email="caio.ariede@gmail.com",
    url="http://github.com/caioariede/django-oscar-cielo",
    license="MIT",
    platforms=["any"],
    packages=['oscar_cielo'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
    install_requires=['django-oscar>=0.2',
                      'python-cielo==0.2'],
)
