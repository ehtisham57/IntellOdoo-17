from odoo import models, fields, api


class Specialization(models.Model):
    _name = 'doctor.specialization'
    _description = 'doctors specialization'

    name = fields.Char(string="Doctor Specialization", required=True)
    doctor_ids = fields.Many2many("my.doctor", string='doctor name')