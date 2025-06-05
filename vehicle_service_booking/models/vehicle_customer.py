from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'vehicle.customer'
    _description = "All customer records"

    name = fields.Char(string= 'Name', required=True)
    phone = fields.Char(string= 'Phone Number', required=True)
    email = fields.Char(string="Email", required=True)

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email:
                pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if not re.match(pattern, record.email):
                    raise ValidationError("Please enter a valid email address.")

    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if record.phone:
                # Basic example: phone should be digits only and 10-15 chars
                pattern = r'^\+?\d{10,15}$'
                if not re.match(pattern, record.phone):
                    raise ValidationError("Please enter a valid phone number (10 to 15 digits, optional +).")
