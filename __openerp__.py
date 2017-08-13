# -*- coding: utf-8 -*-
{
    'name': "City constrains",

    'summary': "This Module Add res_city table to res group and manage partner form in order to restrict keyrring city name at those defined",

    'description': """
        Linked with crm module, the module add 'city' menu
        above localization menu of crm configuration
    """,

    'author': "Nicolas Farrié",
    'website': "http://www.es-natura.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'tool',
    'version': '0.01',
    'application': 'True',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/partner.xml',
        'views/res_city.xml',
        'views/menus.xml',
        # ,
        # 'views/sequence_dossier.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
