from odoo import models, fields, api


class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'
    _description = 'Name of the Customer'
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    order_date = fields.Datetime(default=fields.Datetime.now)

    sale_order_id = fields.Many2one('sale.order', string='Sales Order', ondelete='cascade')
    product_lines = fields.One2many('sale.order.wizard.line', 'line_id', string='Products')

    def action_update_button(self):
        self.ensure_one()
        
        sale_order = self.sale_order_id

        sale_order.order_line.unlink()

        for i in self.product_lines:
            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_id': i.product_template_id.product_variant_id.id,
                'product_uom_qty': i.product_uom_qty,
                'price_unit': i.price_unit,
                'tax_id': [(6, 0, i.tax_id.ids)],
            })

        sale_order.partner_id = self.partner_id
        sale_order.date_order = self.order_date

        return {'type': 'ir.actions.act_window_close'}

