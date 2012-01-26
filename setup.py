from setuptools import setup, find_packages

import dirk

setup(
    name='dirk',
    version=dirk.__version__,
    description='Provide a bridge between Django and IRC.',
    author='James Socol',
    author_email='james@mozilla.com',
    url='https://github.com/jsocol/dirk',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['README.rst']},
    install_requires=['rasputin'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
