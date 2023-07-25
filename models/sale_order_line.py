from odoo import models
from odoo import api
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('price_unit')
    def _onchange_price_unit(self):
        for record in self:
            if record.price_unit > 200:
                record.price_unit = 200
            elif record.price_unit < 0:
                raise UserError('Can\'t set negative unit price')
