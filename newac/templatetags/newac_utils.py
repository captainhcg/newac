from django import template
from settings import STATIC_URL
register = template.Library()

@register.simple_tag
def static_url():
    return STATIC_URL

class VerbatimNode(template.Node):
    def __init__(self, text):
        self.text = text
    
    def render(self, context):
        return self.text

@register.tag
def verbatim(parser, token):
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endverbatim':
            break
        if token.token_type == template.TOKEN_VAR:
            text.append('{{')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('{%')
        text.append(token.contents)
        if token.token_type == template.TOKEN_VAR:
            text.append('}}')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('%}')
    return VerbatimNode(''.join(text))
