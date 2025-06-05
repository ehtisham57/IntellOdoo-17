from odoo import models, fields, api


class Patient(models.Model):
    _name = 'vehicle.record'
    _description = "All vehicles records"

    name = fields.Char(string='Name of vehicle', required=True)
    model = fields.Char(string='Model Of vehicle', required=True)
    no_plate = fields.Char(string="Registration Plate Number", required=True)
    type = fields.Selection([
        ('car', 'Car'),
        ('bike', 'Bike'),
    ], string="Type of vehicle", required=True)

    model_year = fields.Char(string="Model Year", required=True, default='2025')
    
