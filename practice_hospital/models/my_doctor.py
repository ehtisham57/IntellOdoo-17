from odoo import models, fields, api


class Doctor(models.Model):
    _name = 'my.doctor'
    _description = 'all doctors data / table'

    name = fields.Char(string="Name Of Doctor", required=True)
    age = fields.Integer(string="Age Of Doctor")

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender of Doctor')

    doctor_timing = fields.Selection([
        ('morning', 'from 8am to 4pm'),
        ('evening', 'from 4pm to 12am'),
        ('night', 'from 12am to 8am'),
    ], string='Doctor timing in the hospital')

    specialization_ids = fields.Many2many('doctor.specialization', string="Specializations")

    patient_ids = fields.One2many('hos.patient', 'doctor_id', string="Patients")
