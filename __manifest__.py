# -*- coding: utf-8 -*-
{
    'name': "akara_template_widget_demo",

    'summary': """
        this is a demo for template widget""",

    'description': """
        Long description of module's purpose
    """,

    'author': "akara odoo",
    'website': "http://www.awsomeodoo.com",

    'category': 'widget',
    'version': '14.0.0.1',

    'depends': ['base', 'akara_template_widget'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    'qweb': [
        'static/xml/misc.xml'
    ]
}
