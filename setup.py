from setuptools import setup

setup(
    name='t1tp',
    version='0.1.0',
    author='Pierre Formont',
    author_email='pierre.formont@gmail.com',
    description='Python library to retrieve one-time passwords from 1Password',
    license='MIT',
    keywords='t1tp',
    url='https://github.com/tutuchan/t1tp',
    packages=['t1tp'],
    entry_points={
        'console_scripts': [
            't1tp = t1tp.__main__:main'
        ]
    })