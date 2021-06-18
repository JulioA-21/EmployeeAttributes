# -*- coding: utf-8 -*-
{
    'name': "Employee Attributes",

    'summary': """
        Agrega atributos extra al Empleado""",

    'description': """
        Organiza las tareas
    """,

    'author': "Julio",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
       'views/EmpAttribute_view.xml',
    ],
}
