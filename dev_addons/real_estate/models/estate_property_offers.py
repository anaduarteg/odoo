# -*- coding: utf-8 -*-#

from odoo import models, fields


class EstatePropertyOffers(models.Model):
    _name = 'estate.property.offers'

    price = fields.Float(string='Price')
    status = fields.Selection(string='State',
                              selection=[('accepted', 'Accepted'),
                                         ('refused', 'Refused')],
                              copy=False)
    partner_id = fields.Many2one('res.partner', string='Comprador', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)

    def action_accept_offer(self):
        pass

    def action_refuse_offer(self):
        pass