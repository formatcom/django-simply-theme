from django.apps import apps
from django.contrib import admin
from django.urls import reverse
from django.urls import NoReverseMatch
from django.template import Template
from django.utils.text import capfirst
from django.template import Context
from django.template.response import TemplateResponse


class SimplyThemeMiddleware:

    theme = None
    branding = None

    default_site_header = admin.site.site_header

    head_template_code = '''
            <!-- Simply Theme -->
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

    # TODO: valid self.theme is None
    def get_head_content(self):

        template = Template(self.head_template_code)
        context = Context({
            'simply': {
                'theme': { 'xdmin': self.theme.first(), },
            },
        })

        return bytes(template.render(context).encode())

    # TODO: cache here, valid self.theme, self.branding is None
    def patch_branding(self):

        theme = self.theme.first()

        if theme and theme.branding_title_use:

            title = theme.branding_title

            if self.branding.first():
                title = theme.branding_title.replace('[logo]', '[simply.logo]', 1)

            admin.site.site_header = title

        else:
            admin.site.site_header = self.default_site_header


    # TODO: valid self.branding is None
    def render_callback(self, response):

        content = response.content

        content = content.replace(b'</head>', self.get_head_content(), 1)

        branding = self.branding.first()

        # TODO: width height class
        if branding:
            logo = '<img src="{url}" style="max-height:45px" />'.format(**{
                'url': branding.logo.url,
            }).encode()

            content = content.replace(b'[simply.logo]', bytes(logo), 1)

        response.content = content

    # REF: django/contrib/admin/sites.py _build_app_dict
    def build_module_dict(self, request):

        app_dict = {}

        for _model, _admin in admin.site._registry.items():

            app_label = _model._meta.app_label
            app_module = getattr(_admin, 'app_module', app_label)

            has_module_perms = _admin.has_module_permission(request)

            if not has_module_perms:
                continue

            perms = _admin.get_model_perms(request)

            if True not in perms.values():
                continue

            info = (app_label, _model._meta.model_name)

            model_dict = {
                'name': capfirst(_model._meta.verbose_name_plural),
                'object_name': _model._meta.object_name,
                'perms': perms,
                'admin_url': None,
                'add_url': None,
            }

            if perms.get('change') or perms.get('view'):
                model_dict['view_only'] = not perms.get('change')
                try:
                    model_dict['admin_url'] = reverse('admin:%s_%s_changelist' % info, current_app=admin.site.name)
                except NoReverseMatch:
                    pass

            if perms.get('add'):
                try:
                    model_dict['add_url'] = reverse('admin:%s_%s_add' % info, current_app=admin.site.name)
                except NoReverseMatch:
                    pass

            if app_module in app_dict:
                app_dict[app_module]['models'].append(model_dict)
            else:
                app_dict[app_module] = {
                    'name': apps.get_app_config(app_label).verbose_name,
                    'app_label': app_label,
                    'app_url': reverse(
                        'admin:app_list',
                        kwargs={'app_label': app_label},
                        current_app=admin.site.name,
                    ),
                    'has_module_perms': has_module_perms,
                    'models': [model_dict],
                }

        return app_dict

    # TODO: cache here
    def get_module_list(self, request):
        app_dict = self.build_module_dict(request)

        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

        return app_list

    def process_template_response(self, request, response):

        if not self.admin:
            return response

        if isinstance(response, TemplateResponse):

            response.add_post_render_callback(self.render_callback)

            if response.context_data.get('app_list'):
                response.context_data['app_list'] = self.get_module_list(request)

        return response

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

        if apps.is_installed('simply.theme.xdmin'):
            from simply.theme.xdmin.models import Theme
            self.theme = Theme.objects.filter(active=True)

        if apps.is_installed('simply.theme.branding'):
            from simply.theme.branding.models import Branding
            self.branding = Branding.objects.filter(active=True)


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        self.admin = request.path.startswith(reverse('admin:index'))

        if self.admin:
            self.patch_branding()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

