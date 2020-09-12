from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name='DungAF',
    packages=['DungAF'],
    version='1.0',
    license='LGPL v3',
    description='Dung Abstract Argumentation Framework Package.',
    author='Agustina Dinamarca',
    author_email='agustinadinamarca@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/agustinadinamarca/DungAF',
    keywords='Argumentation Framework',
    packages=setup.find_packages(),
    classifiers=['Programming Language :: Python :: 3'],
)
