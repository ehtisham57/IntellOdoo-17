from odoo import models, fields, api
# import re
# from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'vehicle.customer'
    _description = "All customer records"

    name = fields.Char(string= 'Name', required=True)
    phone = fields.Char(string= 'Phone Number', required=True)
    email = fields.Char(string="Email", required=True)

