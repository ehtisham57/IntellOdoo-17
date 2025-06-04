from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Patient(models.Model):
    _name = 'hos.patient'
    _description = 'All patient data / table'
    _inherit = 'hos.person'

    doctor_id = fields.Many2one('my.doctor', string='Doctor Name', required=True)
    selected_dr_timing = fields.Selection(related='doctor_id.doctor_timing', string='Doctor Duty Timing')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft', string="Status", required=True)

    @api.constrains('age')
    def _check_age_not_zero(self):
        for rec in self:
            if rec.age <= 0:
                raise ValidationError("Please enter a valid age greater than 0.")

    def unlink(self):
        for rec in self:
            if rec.doctor_id.name == 'jerry':
                raise UserError("You cannot delete a patient assigned to Dr. Jerry.")
        return super().unlink()

    def print_report(self):
        return self.env.ref('practice_hospital.report_patient').report_action(self)
