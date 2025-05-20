from odoo import models, fields, api


class Specialization(models.Model):
    _name = 'doctor.specialization'
    _description = 'doctors specialization'

    name = fields.Char(string="Doctor Specialization", required=True)

    doctor_id = fields.Many2one("my.doctor", string="Main Doctor")
    doctor_ids = fields.Many2many("my.doctor", string='doctor name')