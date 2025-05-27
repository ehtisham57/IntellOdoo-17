from odoo import models, fields, api


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    add_Field_one = fields.Char(string="My New First Field")
    add_Field_second = fields.Char(string="My New Second Field")
    customer_id = fields.Many2one('res.partner', string='Customer')

    # def action_show_print(self):
    #     print("hello")
    def wiz_open(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order Wizard',
            'res_model': 'sale.order.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_id': self.id,
                'default_partner_id': self.partner_id.id,
                'default_order_date': self.date_order,
            },
        }
