from odoo import models, api

class DeleteSaleOrder(models.Model):
    _inherit = 'sale.order'

    def delete_active_ids(self):
        for record in self:
            invoices = record.invoice_ids
            if invoices:
                invoices.delete_active_ids()

            record.write({'state': 'cancel'})
            record.unlink()

class DeletePurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def delete_active_ids(self):
        for record in self:
            invoices = record.invoice_ids
            if invoices:
                invoices.delete_active_ids()

            record.button_cancel()
            record.unlink()

class DeleteAccountMove(models.Model):
    _inherit = 'account.move'

    def delete_active_ids(self):
        for record in self:
            if record.state not in ['draft', 'cancel']:
                record.button_draft()
            record.unlink()
        