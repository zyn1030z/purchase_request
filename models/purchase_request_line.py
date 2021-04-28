from odoo import fields, models


class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Purchase Request Line'
    _inherit = 'product.product'
    product_request = fields.Many2one('product.product',string='Sản phẩm')

