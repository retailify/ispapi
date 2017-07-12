from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

INSTALL_REQUIREMENTS = [
    'setuptools',
]

setup(
    author='Thomas Meitz',
    author_email='info@retailify.de',
    name='ispapi',
    version="2.2.0",
    description='Hexonet ISP API',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://retailify.de/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)