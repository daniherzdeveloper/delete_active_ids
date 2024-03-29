{
    'name': 'Delete Active IDS',
    'version' : '17.0',
    'summary': 'Delete Active IDS',
    'author': 'daniherzdeveloper@gmail.com',
    'sequence': 10,
    'description': """
        Delete Active IDS
        ================================
        Mass deletion of sales order, purchase order and invoices.
    """,
    'depends': ['base', 'sale', 'purchase', 'account'],
    'category': 'Extra Tools',
    'auto_install': False,
    'data': [
        'views/views.xml',
    ],
    'license': 'LGPL-3',
}