#!/usr/bin/env python
"""Setup to install Bitcoin.de API Python Module."""
from distutils.core import setup
setup(name='btcde',
      version='1.3',
      py_modules=['btcde'],
      install_requires=['requests', 'future'],
      description='Provides functions to work with Bitcoin.de Trading API.',
      url='https://github.com/peshay/btcde',
      author='Andreas Hubert',
      author_email='anhubert@gmail.com',
      license='MIT',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Libraries :: Application '
                   'Frameworks',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6', ],
      keywords='bitcoin.de bitcoin btc api',

      )
