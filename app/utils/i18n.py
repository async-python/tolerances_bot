"""TranslatorHub module."""

from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    """Create and setup translator_hub."""
    translator_hub = TranslatorHub(
        {"ru": ("ru", "en"), "en": ("en", "ru")},
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=["app/locales/ru/LC_MESSAGES/txt.ftl"],
                ),
            ),
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US",
                    filenames=["app/locales/en/LC_MESSAGES/txt.ftl"],
                ),
            ),
        ],
    )
    return translator_hub
