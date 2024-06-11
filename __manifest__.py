{
    'name': 'My Odoo Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manage collections and import from Rails app',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/collection_views.xml',
    ],
    'installable': True,
    'application': True,
}

