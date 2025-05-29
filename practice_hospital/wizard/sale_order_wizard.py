from odoo import models, fields, api


class SaleOrderWizard(models.TransientModel):
    _name = 'sale.order.wizard'
    _description = 'Name of the Customer'

    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    order_date = fields.Datetime(default=fields.Datetime.now)

    # yahan sale order call kia hay

    sale_order_id = fields.Many2one('sale.order', string='Sales Order', ondelete='cascade')

    # yahan sale order may say values aarahi hain. product, sale waghera. id vise many value aarahi hain jo order_id mai save ho rahi hain

    product_lines = fields.One2many('sale.order.wizard.line', 'wizard_id', string='Products')

    def action_add_button(self):
        # yeh aaik aaik record ko laa kar daita hay
        self.ensure_one()

        # yahan sale order main apna sale order safe kia hay. basically yahan aaik variable banaya hay sale_order naam ka. ismain sale_order_id ko set kia hay.
        # aagay saray product isi kay zariye call hongay

        sale_order = self.sale_order_id

        # jo product_line aarahi hai us main loop lagaya hay. q kay jo poducts hum select karaingay aaaik aaik kar kay sari products add kar daiga yeh is main
        # with the help of loop

        for i in self.product_lines:
            # sale.order.line jo kay model hay jahan say products aarahi hain wahan yeh sub products line ko bari bari create kardaiga

            self.env['sale.order.line'].create({
                'order_id': sale_order.id,
                'product_id': i.product_template_id.product_variant_id.id,
                'product_uom_qty': i.product_uom_qty,
                'price_unit': i.price_unit,
                'tax_id': [(6, 0, i.tax_id.ids)],
            })

        # jb lines add hojaaingi to jo partner select kia hay or jo date select ki hay woh bhy update hojaaiga.

        sale_order.partner_id = self.partner_id
        sale_order.date_order = self.order_date

        # sub honay kay bd wizard / form band hojaiga

        return {'type': 'ir.actions.act_window_close'}
