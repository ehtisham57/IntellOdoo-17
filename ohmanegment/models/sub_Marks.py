from odoo import models, fields, api

class SubjectLine(models.Model):
    _name = 'my.subject.line'

    subject_id = fields.Many2one('my.subject', string='Subject')
    marks = fields.Integer(string='Marks')
    student_id = fields.Many2one('my.student', string='Student')
