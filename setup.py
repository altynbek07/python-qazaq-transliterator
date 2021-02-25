from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qazaq_transliterator',
    version='2.0',
    description='Transliteration of the old Kazakh alphabet into a new one',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Altynbek',
    author_email='altynbek.kazezov.97@gmail.com',
    url='https://github.com/altynbek07/python-qazaq-transliterator',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    keywords='translit, transliteration, transliterator, qazaq, kazakh, python, latin',
    packages=find_packages(),
    install_requires=[
        'transliterate>=1.10.2'
    ],
    test_suite='tests'
)
