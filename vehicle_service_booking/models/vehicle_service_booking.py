from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.populate import compute


class Patient(models.Model):
    _name = 'vehicle.service.booking'
    _description = "All booking records"

    customer_id = fields.Many2one('vehicle.customer', string='Select Customer', required=True)
    preferred_date = fields.Date(string='Preferred Date', required=True)
    issue_description = fields.Text(string='Description')
    price = fields.Integer(string='Actual Amount', required=True)
    advance = fields.Integer(string='Advance Amount')
    balance = fields.Integer(string='Balance Amount', compute='_on_change_amount')

    vehicle_ids = fields.Many2many('vehicle.record', compute="_compute_names")

    # vehicle_names = fields.Char(string="Vehicle Names", compute="_compute_names")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft', string="Status", required=True)

    def open_wizard(self):
        # print(self.vehicle_ids.ids)
        return {
            'type': 'ir.actions.act_window',
            'name': 'vehicle selection',
            'res_model': 'vehicle.selection.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_ids': self.ids,
                'default_vehicle_ids': self.vehicle_ids.ids,
                'default_price': self.price,
                'default_advance': self.advance
            },
        }

    @api.depends('vehicle_ids')
    def _compute_names(self):
        for rec in self:
            for customer in rec.vehicle_ids:
                vehicle_name = self.env['vehicle.record'].search([('name', '=', customer.name)])
                vehicle_ids = vehicle_name
                pass

    # @api.depends('vehicle_ids')
    # def _compute_names(self):
    #     for i in self:
    #         get_name = i.vehicle_ids.mapped('name')
    #         vehicle_ids = get_name

    @api.onchange('price', 'advance')
    def _on_change_amount(self):
        for i in self:
            i.balance = (i.price) - (i.advance)

    def unlink(self):
        for rec in self:
            if rec.state in self.state == 'done':
                raise UserError("You cannot delete confirmed booking.")
        return super().unlink()
