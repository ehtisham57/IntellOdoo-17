from odoo import models, fields, api


class SaleOrderWizardLine(models.TransientModel):
    _name = 'sale.order.wizard.line'

    # yeh wizard id hay jo sale order wizard may jaa rahi ha. mujhay product par One2Many field lagani thy or Many2one aarahi thy.
    # to iskay ziriye mainay many products aaik time main bhaij diye
    line_id = fields.Many2one('sale.order.wizard', required=True)

    # yeh tamam field product add karnay ki hain
    product_template_id = fields.Many2one('product.template', string='Product', required=True)
    product_uom_qty = fields.Float(string='Quantity', required=True)
    price_unit = fields.Float(string='Unit Price', required=True)
    tax_id = fields.Many2many('account.tax', string='Taxes')
