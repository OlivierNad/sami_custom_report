# -*- coding: utf-8 -*-
{
    'name': "ods_custom_report",

    'summary': """
        ods_report module for custom report""",

    'description': """
        ods_report module for custom report
    """,

    'author': "GandG Professional Services",
    'website': "http://www.gandgcorp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase', 'sale_management', 'sale_project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/custom_header_footer.xml',
        'views/external_layout.xml',
        'reports/report_sale_order.xml',
        'reports/report_account_move.xml',
        #'reports/menu_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}