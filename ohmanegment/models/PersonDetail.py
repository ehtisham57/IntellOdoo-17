from odoo import models, fields


class PersonDetail(models.Model):
    _name = 'hos.person'
    _description = 'Hospital Person'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
