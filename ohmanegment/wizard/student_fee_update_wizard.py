from odoo import models, fields, api


class StudentFeeUpdateWizard(models.TransientModel):
    _name = 'student.fee.update.wizard'
    _description = 'Student Fee Update Wizard'

    total_fee = fields.Float(string='Fees')

    def update_student_fees(self):
        self.env['my.student'].browse(self._context.get('active_ids')).update({'total_fee':self.total_fee})
        return True