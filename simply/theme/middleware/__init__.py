from django.contrib import admin
from django.urls import reverse
from django.template import Template
from django.template import Context
from django.template.response import TemplateResponse

from simply.theme.xdmin.models import Theme


class SimplyThemeMiddleware:

    queryset = Theme.objects.filter(active=True)

    default_site_header = admin.site.site_header

    head_template_code = '''
            <style>

                {% if simply.theme.xdmin.branding_bg_color_use %}
                #branding
                {
                    background: {{simply.theme.xdmin.branding_bg_color}};
                }
                {% endif %}

                {% if simply.theme.xdmin.branding_text_color_use %}
                #branding, #branding h1
                {
                    color: {{simply.theme.xdmin.branding_text_color}};
                }
                {% endif %}

                {% if simply.theme.xdmin.branding_link_color_use %}
                #branding a:link, #branding a:visited,
                #branding h1 a:link, #branding h1 a:visited
                {
                    color: {{simply.theme.xdmin.branding_link_color}};
                }
                {% endif %}

                {% if simply.theme.xdmin.branding_link_hover_color_use %}
                #branding a:focus, #branding a:hover,
                #branding h1 a:focus, #branding h1 a:hover
                {
                    color: {{simply.theme.xdmin.branding_link_hover_color}};
                }
                {% endif %}

                #header
                {

                {% if simply.theme.xdmin.header_bg_color_use %}
                    background: {{simply.theme.xdmin.header_bg_color}};
                {% endif %}

                {% if simply.theme.xdmin.header_text_color_use %}
                    color: {{simply.theme.xdmin.header_text_color}};
                {% endif %}

                }

                {% if simply.theme.xdmin.header_link_color_use %}
                #header a:link, #header a:visited
                {
                    color: {{simply.theme.xdmin.header_link_color}};
                }
                {% endif %}

                {% if simply.theme.xdmin.header_link_hover_color_use %}
                #header a:focus, #header a:hover
                {
                    color: {{simply.theme.xdmin.header_link_hover_color}};
                }
                {% endif %}

                div.breadcrumbs
                {

                {% if simply.theme.xdmin.breadcrumbs_bg_color_use %}
                    background: {{simply.theme.xdmin.breadcrumbs_bg_color}};
                {% endif %}

                {% if simply.theme.xdmin.breadcrumbs_text_color_use %}
                    color: {{simply.theme.xdmin.breadcrumbs_text_color}};
                {% endif %}

                }

                {% if simply.theme.xdmin.breadcrumbs_link_color_use %}
                div.breadcrumbs a:link, div.breadcrumbs a:visited
                {
                    color: {{simply.theme.xdmin.breadcrumbs_link_color}};
                }
                {% endif %}

                {% if simply.theme.xdmin.breadcrumbs_link_hover_color_use %}
                div.breadcrumbs a:focus, div.breadcrumbs a:hover
                {
                    color: {{simply.theme.xdmin.breadcrumbs_link_hover_color}};
                }
                {% endif %}

                .module h2, .module caption, .inline-group h2
                {

                {% if simply.theme.xdmin.module_bg_color_use %}
                    background: {{simply.theme.xdmin.module_bg_color}};
                {% endif %}

                {% if simply.theme.xdmin.module_text_color_use %}
                    color: {{simply.theme.xdmin.module_text_color}};
                {% endif %}

                }

                {% if simply.theme.xdmin.module_link_color_use %}
                .module a:link, .module a:visited
                {
                    color: {{simply.theme.xdmin.module_link_color}};
                }
                {% endif %}

                {% if simply.theme.xdmin.module_link_hover_color_use %}
                .module a:focus, .module a:hover
                {
                    color: {{simply.theme.xdmin.module_link_hover_color}};
                }
                {% endif %}

            </style>
        </head>
    '''

    body_template_code = '''
        </body>
    '''

    def get_head_content(self):

        template = Template(self.head_template_code)
        context = Context({
            'simply': {
                'theme': { 'xdmin': self.queryset.first(), },
            },
        })

        return bytes(template.render(context).encode())

    # TODO: working
    def get_body_content(self):
        return ''

    def render_callback(self, response):


        theme = self.queryset.first()

        if not theme:
            admin.site.site_header = self.default_site_header
            return None

        response.content = response.content.replace(b'</head>', self.get_head_content(), 1)

        if theme.branding_title_use:
            admin.site.site_header = theme.branding_title
        else:
            admin.site.site_header = self.default_site_header


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
