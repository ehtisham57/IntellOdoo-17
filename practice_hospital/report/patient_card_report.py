from odoo import models, fields, api


class PatientCardReport(models.AbstractModel):
    _name = "report.practice_hospital.report_patient_template"
    _description = "Patient Card Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['hos.patient'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hos.patient',
            'docs': docs,
            'data': data,
        }
