import setuptools

import ig

packages = setuptools.find_packages(exclude=[
    'tests',
    'tests.integration',
    'tests.unit'
])
requires = [
    'requests',
    "pycryptodome"
]


setuptools.setup(
   name='ig',
   version=ig.__version__,
   description='IG REST API python library',
   author='Denis Volokh',
   author_email='denis.volokh@gmail.com',
   packages=packages,
   install_requires=requires
)
