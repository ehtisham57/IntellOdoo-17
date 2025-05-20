from odoo import models, fields, api

class Doctor(models.Model):
    _name = 'my.doctor'
    _description = 'All doctors data / table'
    _inherit = 'hos.person'

    doctor_timing = fields.Selection([
        ('morning', 'from 8am to 4pm'),
        ('evening', 'from 4pm to 12am'),
        ('night', 'from 12am to 8am'),
    ], string='Doctor Timing in the Hospital')

    specialization_ids = fields.Many2many('doctor.specialization', string="Specializations")

    patient_ids = fields.One2many('hos.patient', 'doctor_id', string="Patients")
