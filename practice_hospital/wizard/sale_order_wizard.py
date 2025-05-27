import datetime

from odoo import models, fields, api


class SaleOrderWizard(models.TransientModel):
    # _inherit = 'sale.order'
    _name = 'sale.order.wizard'
    _description = 'name of the customer'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    order_date = fields.Datetime()
    product_template_id = fields.Many2one('product.template', string='product template')
    product_uom_qty = fields.Float(string="Quantity", required=True)
    price_unit = fields.Float(string="Unit Price", required=True)
    tax_id = fields.Many2many('account.tax', string="Taxes")

    def action_update_button(self):
        print(self)

