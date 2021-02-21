# Python Qazaq Transliterator

[![PyPI Version](https://img.shields.io/pypi/v/qazaq-transliterator.svg)](https://pypi.python.org/pypi/qazaq-transliterator)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/qazaq-transliterator.svg)](https://pypi.python.org/pypi/qazaq-transliterator/)

![Qazaq Transliterator](https://tengrinews.kz/userdata/news/2017/news_315984/photo_212587.jpg)

Transliteration of the old Kazakh alphabet into a new one. Inspired by [barseghyanartur/transliterate](https://github.com/barseghyanartur/transliterate)

## Prerequisites

- Python >=2.7, >=3.4, PyPy

## Installation

Install with latest stable version from PyPI:

```bash
pip install qazaq-transliterator
```

## Usage

```python
from qazaq_transliterator import translit

text = "Қазақстан Республикасы — Шығыс Еуропа мен Орталық Азияда орналасқан мемлекет."

print(translit(text))
# Qazaqstan Respublikasy — Şyğys Europa men Ortalyq Aziiada ornalasqan memleket.
```

## Testing

```bash
python setup.py test
```

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) for details.

## Security

If you discover any security related issues, please email altynbek.kazezov.97@gmail.com instead of using the issue tracker.

## Credits

- [Altynbek](https://github.com/altynbek07)
- [All Contributors](../../contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
