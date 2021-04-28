# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Request',
    'version': '1',
    'category': '',
    'author': 'hungpham',
    'sequence': 1,
    'summary': 'Purchase Request information',
    'description': "",
    'website': '',
    'images': [
    ],
    'depends': [
        'purchase',
    ],
    'data': [
        'security/ir.model.access.csv',
        'view/purchase_request.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [''],
}
