from odoo import models, fields, api


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    add_Field_one = fields.Char(string="My New First Field")
    add_Field_second = fields.Char(string="My New Second Field")

    customer_id = fields.Many2one('res.partner', string='Customer')

    def action_show_print(self):
        print("hello")
