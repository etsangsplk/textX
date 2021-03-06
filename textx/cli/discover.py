import click

from textx.registration import (language_descriptions,
                                generator_descriptions)


def list_languages(textx):
    @textx.command()
    def list_languages():
        """
        List all registered languages
        """
        for language in language_descriptions().values():
            click.echo("{:<30}{:<30}{}".format("{} ({})"
                                               .format(language.name,
                                                       language.pattern),
                                               language.project_name,
                                               language.description))


def list_generators(textx):
    @textx.command()
    def list_generators():
        """
        List all registered generators
        """
        for language in generator_descriptions().values():
            for generator in language.values():
                click.echo("{:<30}{:<30}{}".format("{} -> {}"
                                                   .format(generator.language,
                                                           generator.target),
                                                   generator.project_name,
                                                   generator.description))
