from odoo import models, api

class DeleteSaleOrder(models.Model):
    _inherit = 'sale.order'

    def delete_active_ids(self):
        self.write({'state': 'cancel'})
        self.unlink()

class DeletePurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def delete_active_ids(self):
        self.write({'state': 'cancel', 'mail_reminder_confirmed': False})
        self.unlink()

class DeleteAccountMove(models.Model):
    _inherit = 'account.move'

    def delete_active_ids(self):
        self.button_draft()
        self.unlink()