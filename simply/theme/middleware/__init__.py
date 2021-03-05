from django.urls import reverse
from django.template import Template
from django.template import Context
from django.template.response import TemplateResponse

from simply.theme.xdmin.models import Theme


class SimplyThemeMiddleware:

    head_template_code = '''
            <style>
                #header {

                {% if simply.theme.xdmin.header_bg_color %}
                    background: {{simply.theme.xdmin.header_bg_color}};
                {% endif %}

                {% if simply.theme.xdmin.header_text_color %}
                    color: {{simply.theme.xdmin.header_text_color}}
                {% endif %}

                }
            </style>
        </head>
    '''

    body_template_code = '''
        </body>
    '''

    def get_head_content(self):

        theme = Theme.objects.filter(active=True).first()

        if not theme:
            return b''

        template = Template(self.head_template_code)
        context = Context({
            'simply': {
                'theme': { 'xdmin': theme, },
            },
        })

        return bytes(template.render(context).encode())

    # TODO: working
    def get_body_content(self):
        return ''

    def render_callback(self, response):

        head_content = self.get_head_content()

        if head_content:
            response.content = response.content.replace(b'</head>', head_content, 1)

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        if not request.path.startswith(reverse('admin:index')):
            return response

        if isinstance(response, TemplateResponse):
            response.add_post_render_callback(self.render_callback)

        return response
