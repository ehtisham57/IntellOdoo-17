from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'my.teacher'
    _description = 'Teacher Record'
    _inherit = 'hos.person'

    # name = fields.Char(string="Name", required=True)
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female'),
    #     ('other', 'Other'),
    # ], string='Gender')

    type_teacher = fields.Selection([
        ('primary', 'Primary Teacher'),
        ('secondary', 'Secondary Teacher'),
        ('h_secondary', 'Higher Secondary Teacher'),
    ], string='Teacher Type', default='primary')

    sequence = fields.Integer(default=10)
    _order = 'sequence,id'

    # If each teacher teaches one subject
    subject_id = fields.Many2one('my.subject', string='Subjects')

    # Teachers actions

    def action_primary(self):
        for rec in self:
            rec.type_teacher = 'primary'

    def action_secondary(self):
        for rec in self:
            rec.type_teacher = 'secondary'

    def action_h_secondary(self):
        for rec in self:
            rec.type_teacher = 'h_secondary'

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.name = self.name.capitalize()
