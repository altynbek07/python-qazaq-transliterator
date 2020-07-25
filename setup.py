from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qazaq_transliterator',
    version='0.1.3',
    description='Transliteration of the old Kazakh alphabet into a new one',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Altynbek',
    author_email='altynbek.kazezov.97@gmail.com',
    url='https://github.com/altynbek07/python-qazaq-transliterator',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=[
        'transliterate>=1.10.2'
    ]
)
