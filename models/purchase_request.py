from odoo import fields, models

from odoo import fields, models


class PurchaseRequest(models.Model):
    _name = "purchase.request"
    # _inherit = 'purchase.order'
    # _inherit = 'purchase.request.line'
    _description = "Purchase Request"
    name = fields.Text(string="Số phiếu")
    requested_by = fields.Selection([
        ('draft', 'user dang nhap'),
        ('in_use', 'user1'),
    ],
        string='Người yêu cầu', track_visibility='always', default='draft'
    )
    department = fields.Selection([
        ('draft', 'user dang nhap'),
        ('in_use', 'user1'),
    ],
        string='Bộ phận', track_visibility='always', default='draft'
    )
    cost_total = fields.Text(string="Tổng chi phí")
    creation_date = fields.Date(string="Ngày yêu cầu")
    due_date = fields.Date(string="Ngày cần cấp")
    approved_date = fields.Date(string="Ngày phê duyệt")
    company = fields.Selection([
        ('draft', 'user dang nhap'),
        ('in_use', 'user1'),
    ],
        string='Công ty', track_visibility='always', default='draft'
    )
    reject_reason = fields.Text(string="Lý do từ chối duyệt")
    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('sent', 'Chờ duyệt'),
        ('to approve', 'Đã duyệt'),
        ('done', 'Hoàn thành'),
        ('cancel', 'Hủy')]
        , string='Status', default='draft',track_visibility='always',)
