from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.populate import compute


class Patient(models.Model):
    _name = 'vehicle.service.booking'
    _description = "All booking records"

    customer_id = fields.Many2one('vehicle.customer', string='Select Customer')
    vehicle_ids = fields.Many2one('vehicle.record')
    preferred_date = fields.Date(string='Preferred Date')
    issue_description = fields.Text(string='Description')

    price = fields.Integer(string='Actual Amount')
    advance = fields.Integer(string='Advance Amount')
    balance = fields.Integer(string='Balance Amount', compute='_on_change_amount')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft', string="Status", required=True)

    @api.onchange('price', 'advance')
    def _on_change_amount(self):
        for i in self:
            i.balance = (i.price) - (i.advance)

    def unlink(self):
        for rec in self:
            if rec.state == 'done':
                raise UserError("You cannot delete confirmed booking.")
        return super().unlink()
