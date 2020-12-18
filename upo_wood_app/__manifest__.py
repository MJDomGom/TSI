# -*- coding: utf-8 -*-
{
    'name': "UpoWood_app",

    'summary': """
        Sumario del modulo UPOWOOD""",

    'description': """
        Descripcion del modulo UPOWOOD
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/proveedor_report.xml',
        'views/producto.xml',
        'views/venta.xml',
        'views/devolucion.xml',
        'views/envio.xml',
        'views/albaran.xml',
        'views/persona.xml',
        'views/factura.xml',
        'views/categoria.xml',
        'views/material.xml',
        'views/proveedor.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
