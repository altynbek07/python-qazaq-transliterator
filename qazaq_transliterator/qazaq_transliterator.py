# -*- coding: utf-8 -*-

from transliterate import get_translit_function
from transliterate.base import TranslitLanguagePack, registry


class KazakhLanguagePack(TranslitLanguagePack):
    language_code = "kk"
    language_name = "Kazakh"

    mapping = (
        u"аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцшъыіьэАӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦШЪЫІЬЭ",
        u"aäbvgğdeejziikqlmnŋoöprstuūüfhhcş'yı'eAÄBVGĞDEEJZİİKQLMNŊOÖPRSTUŪÜFHHCŞ'YI'E"
    )

    # TODO
    # reversed_specific_mapping = (
    # )

    # TODO
    # reversed_specific_pre_processor_mapping = {
    # }

    pre_processor_mapping = {
        u"ч": u"ch",
        u"щ": u"şh",
        u"ю": u"iu",
        u"я": u"ia",
        u"Ч": u"Ch",
        u"Щ": u"Şh",
        u"Ю": u"İu",
        u"Я": u"İa",
    }


registry.register(KazakhLanguagePack)

translit_kk = get_translit_function("kk")


def translit(value: str) -> str:
    """Transliterate the text."""
    return translit_kk(value)
