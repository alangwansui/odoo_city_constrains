# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = 'res.partner'

    ### Add a new column to the res.partner model, to constrains city
    # from a res_partner_city table where state_id  is mandatory and point to a country id which is mandatory too
    # original fields are : (in class res.partner (file res_partner.py)
    # see it at https: // fossies.org / dox / odoo - 8.0.0 / openerp_2addons_2base_2res_2res__partner_8py_source.html
    # line:265/:  'city': fields.char('City'),
    # line:266/:  'state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
    # line:267/:  'country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),
    ###

    city_id = fields.Many2one(
        comodel_name="res.city",
        string="City"
    )
    state_id_name = fields.Char(
        related="city_id.state_id.name",
        string="State",
        index=True
    )
    country_id_name = fields.Char(
        related="city_id.state_id.country_id.name",
        string='Country',
        index=True
    )

    @api.one
    @api.onchange('city_id')
    def _onchange_city(self):
        if self.city_id:
            if self.city_id.zip_code:
                self.zip = self.city_id.zip_code

    @api.constrains('city_id','zip')
    def set_state_country(self):
        for r in self:
            if r.city_id:
                r.city = r.city_id.name
                r.state_id = r.city_id.state_id
                r.country_id = r.city_id.state_id.country_id


class City(models.Model):
    _name = 'res.city'

    name = fields.Char(
        string='City'
    )
    airport_code = fields.Char(
        string='Airport Code',
        size=3
    )
    zip_code = fields.Char(
        string="ZIP",
        help="Not mandatory: leave blank if there is more than on zip code for this town")

    state_id = fields.Many2one(
        string="State",
        comodel_name='res.country.state'
    )
    country_id_name = fields.Char(
        related="state_id.country_id.name",
        string='Country',
        index=True
    )




