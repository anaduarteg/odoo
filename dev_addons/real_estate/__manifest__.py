# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': "Real Estate Applicaction - Odoo17 Tutorial",

    'description': """
       This is a Tutorial for the creation of a new Module in Odoo17
       The module implemented is a simple Real Estate App 
    """,

    'author': 'U Comunera',

    'category': 'Uncategorized',

    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_menu.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_type_menu.xml',
        'views/estate_property_tags_views.xml',
        'views/estate_property_tags_menu.xml',
        'views/estate_property_offers_views.xml'
    ],

    'demo': [
    ],

    "qweb": [
    ],

    'installable': True
}

