from transliterate import get_translit_function
from transliterate.base import TranslitLanguagePack, registry


class KazakhLanguagePack(TranslitLanguagePack):
    language_code = "kk"
    language_name = "Kazakh"

    mapping = (
        u"аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцъыіьэАӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЪЫІЬЭ",
        u"aábvgǵdeejzııkqlmnńoóprstýuúfhhc'yi'eAÁBVGǴDEEJZIIKQLMNŃOÓPRSTÝUÚFHHC'YI'E"
    )

    # TODO
    # reversed_specific_mapping = (
    # )

    # TODO
    # reversed_specific_pre_processor_mapping = {
    # }

    pre_processor_mapping = {
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"sch",
        u"ю": u"ıý",
        u"я": u"ıa",
        u"Ч": u"Ch",
        u"Ш": u"Sh",
        u"Щ": u"Sch",
        u"Ю": u"Iý",
        u"Я": u"Ia",
    }


registry.register(KazakhLanguagePack)

translit_kk = get_translit_function("kk")

def translit(value: str) -> str:
    """Transliterate the text."""
    return translit_kk(value)