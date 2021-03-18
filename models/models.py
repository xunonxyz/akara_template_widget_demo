# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class AkaraTempalteWidget(models.Model):
    '''
    tempate widget demo
    '''
    _name = 'akara_template_widget_demo.akara_template_widget_demo'
    _description = 'akara_template_widget_demo.akara_template_widget_demo'

    name = fields.Char()
    value = fields.Integer()
    value3 = fields.Boolean(string="test val")
    value2 = fields.Float(compute="_value_pc", store=True)
    test_image = fields.Image(string="test", attachment=False)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        '''
        compute
        :return:
        '''
        for record in self:
            record.value2 = float(record.value) / 100

    def accept_callback(self):
        '''
        success callback
        :return:
        '''
        raise exceptions.ValidationError('accept callback is called')

    def reject_callback(self):
        '''
        success callback
        :return:
        '''
        raise exceptions.ValidationError('reject callback is called')

    def change_callback(self):
        '''
        change callback
        :return:
        '''
        if self.name:
            self.name = False
        else:
            self.name = 'name is changed'
