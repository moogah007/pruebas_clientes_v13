# -*- coding: utf-8 -*-

from odoo import http, models, fields, api, _, tools, registry
from odoo.exceptions import ValidationError, UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def default_get(self, fields):
        res = super(ProductTemplate, self).default_get(fields)
        res.update({'purchase_ok': False})
        return res
