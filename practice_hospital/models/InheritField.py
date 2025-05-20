from odoo import models, fields, api

class InheritSaleOrder(models.Model):
    _inherit = 'my.teacher'

    custom_field = fields.Char(string="Custom Field Added")
