from docutils import nodes
from docutils.parsers.rst import directives, Directive
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.special import TextLexer
from radpress.solarized import SolarizedStyle
from radpress.settings import MORE_TAG

DEFAULT = HtmlFormatter(style=SolarizedStyle)
VARIANTS = {
    'linenos': HtmlFormatter(style=SolarizedStyle, linenos=True),
}


class Pygments(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = dict([(key, directives.flag) for key in VARIANTS])
    has_content = True

    def run(self):
        self.assert_has_content()
        try:
            lexer = get_lexer_by_name(self.arguments[0])
        except ValueError:
            # no lexer found - use the text one instead of an exception
            lexer = TextLexer()
        # take an arbitrary option if more than one is given
        formatter = (
            self.options and VARIANTS[self.options.keys()[0]] or DEFAULT)
        parsed = highlight(u'\n'.join(self.content), lexer, formatter)
        return [nodes.raw('', parsed, format='html')]


class More(Directive):

    def run(self):
        return MORE_TAG
