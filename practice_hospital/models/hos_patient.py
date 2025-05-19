from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from odoo.tools.populate import compute


class Patient(models.Model):
    _name = 'hos.patient'
    _description = 'all patient data / table'

    name = fields.Char(string="Name Of patient", required=True)
    age = fields.Integer(string="Age Of patient", required=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender of patient', required=True)

    doctor_id = fields.Many2one('my.doctor', string='Doctor Name', required=True)

    selected_dr_timing = fields.Selection(related='doctor_id.doctor_timing', string='Doctor Duty Timing')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft', string="Status", required=True)

    # def action_done(self):
    #     for rec in self:
    #         if not rec.name or not rec.doctor_id:
    #             raise ValidationError("Please fill all required fields.")
    #         rec.state = 'done'
    #
    # def action_cancel(self):
    #     for rec in self:
    #         rec.state = 'cancel'
    #
    # def action_draft(self):
    #     for rec in self:
    #         rec.state = 'draft'

    @api.constrains('age')
    def _check_age_not_zero(self):
        for rec in self:
            if rec.age <= 0:
                raise ValidationError("Please Enter a valid age.....")

    def unlink(self):
        for rec in self:
            if rec.doctor_id.name == 'jerry':
                raise UserError("You cannot delete patient of jerry.")
        return super().unlink()
