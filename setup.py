import os

from setuptools import setup, find_packages

module_path = os.path.join(os.path.dirname(__file__), 'barrelmagazine', '__init__.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setup(name='barrelmagazine',
      version=__version__,
      description='A thread-safe LRU caching for Python 3.',
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='decorator lazy attribute property',
      author='Chuong Ngo',
      author_email='cngo.github@gmail.com',
      url='https://github.com/cngo-github/barrel-magazine',
      license='MIT License',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      test_suite='barrelmagazine.tests',
      install_requires=['cachetools']
)
