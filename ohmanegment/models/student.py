from odoo import models, fields, api


class Student(models.Model):
    _name = 'my.student'
    _description = 'Student Record'
    _inherit = 'hos.person'

    # name = fields.Char(string="Name", required=True)
    # age = fields.Integer(string="Age")
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'Other'),
    # ], string='Gender')

    class_name = fields.Char(string="Class")
    section = fields.Selection([
        ('a', 'A'), ('b', 'B'), ('c', 'C'),
    ])

    subject_ids = fields.Many2many('my.subject', 'subject_id')
    subject_line_ids = fields.One2many('my.subject.line', 'student_id', string='Subjects')
    total_marks = fields.Integer(string='Total Marks', compute='_compute_total_marks', store=True)

    total_fee = fields.Float(string='Fee Amount')

    percentage = fields.Float(string='Percentage', compute='_compute_percentage', store=True)

    @api.depends('subject_line_ids.marks')
    def _compute_total_marks(self):
        for rec in self:
            rec.total_marks = sum(line.marks for line in rec.subject_line_ids)

    @api.onchange('subject_ids')
    def _onchange_subject_ids(self):
        self.subject_line_ids = [(5, 0, 0)]
        lines = []
        for subject in self.subject_ids:
            lines.append((0, 0, {'subject_id': subject.id, 'marks': 0}))

        self.subject_line_ids = lines

    def wiz_open(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Update Fees',
            'res_model': 'student.fee.update.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_ids': self.ids,
                'default_total_fee': self.total_fee,
            },
        }

    @api.depends('total_marks', 'subject_ids')
    def _compute_percentage(self):
        for rec in self:
            rec.percentage = (rec.total_marks / (len(rec.subject_ids) * 100)) * 100 if rec.subject_ids else 0.0

    # FOR DELETE ODOO HAS IT'S OWN METHOD / Before deleting any record it would by confirmed you

    def unlink(self):
        return super().unlink()
