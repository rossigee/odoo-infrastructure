# -*- coding: utf-8 -*-
{
    'name': "posix_accounts",

    'summary': """
        Adds POSIX user information fields.""",

    'description': """
        Adds POSIX fields to Odoo user records and a POSIX groups table. This allows other applications to use the Odoo users and groups data as a Single Source Of Truth for an enterprise-wise RBAC service.""",

    'author': "Ross Golder",
    'website': "https://www.golder.org",

    'category': 'Infrastructure',
    'version': '12.0.1.0.0',

    'depends': [
        'base',
    ],

    'data': [
        'views/user.xml',
    ],
}
