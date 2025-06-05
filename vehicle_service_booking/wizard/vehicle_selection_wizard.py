from odoo import models, fields, api


class SaleOrderWizard(models.TransientModel):
    _name = 'vehicle.selection.wizard'
    _description = 'vehicle selection wizard'

    booking_id = fields.Many2one('vehicle.service.booking', ondelete='cascade')

    vehicle_ids = fields.Many2many('vehicle.record')

    price = fields.Integer(string='Actual Amount', required=True)
    advance = fields.Integer(string='Advance Amount')

    def action_update_button(self):
        self.env['vehicle.service.booking'].browse(self._context.get('active_ids')).update({
            'vehicle_ids': self.vehicle_ids,
            'price': self.price,
            'advance': self.advance
        })
