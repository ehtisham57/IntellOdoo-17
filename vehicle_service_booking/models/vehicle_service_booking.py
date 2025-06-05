
from odoo import models, fields, api


class Patient(models.Model):
    _name = 'vehicle.service.booking'
    _description = "All booking records"

    customer_id = fields.Many2one('vehicle.customer', string='Select Customer')
    vehicle_ids = fields.Many2many('vehicle.record')
    preferred_date = fields.Date(string='Preferred Date')
    issue_description = fields.Text(string='Description')