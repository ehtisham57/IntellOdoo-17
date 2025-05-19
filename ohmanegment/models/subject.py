# subject.py
from odoo import models, fields

class Subject(models.Model):
    _name = 'my.subject'
    _description = 'Subjects for Students and Teachers'

    name = fields.Char(string="Subject Name", required=True )
    code = fields.Char(string="Subject Code")
    teacher_id = fields.Many2one('my.teacher', string="Teacher")
    student_ids = fields.Many2many('my.student', string="Students")