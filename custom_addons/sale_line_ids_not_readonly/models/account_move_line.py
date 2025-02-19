from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move.line"
    
    sale_line_ids = fields.Many2many(
        'sale.order.line',
        'sale_order_line_invoice_rel',
        'invoice_line_id', 'order_line_id',
        string='Sales Order Lines', readonly=False, copy=False)

    