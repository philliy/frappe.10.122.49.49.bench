# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe.utils.make_random import how_many, can_make, get_random
from frappe.utils import cstr
from frappe.desk import query_report
from erpnext.setup.utils import get_exchange_rate
from erpnext.accounts.party import get_party_account_currency
from erpnext.exceptions import InvalidCurrency

def run_purchase(current_date):
	# make material requests for purchase items that have negative projected qtys
	if can_make("Material Request"):
		report = "Items To Be Requested"
		for row in query_report.run(report)["result"][:how_many("Material Request")]:
			make_material_request(current_date, row[0], -row[-1])

	# get supplier details
	supplier = get_random("Supplier")

	company_currency = frappe.db.get_value("Company", "Wind Power LLC", "default_currency")
	party_account_currency = get_party_account_currency("Supplier", supplier, "Wind Power LLC")
	if company_currency == party_account_currency:
		exchange_rate = 1
	else:
		exchange_rate = get_exchange_rate(party_account_currency, company_currency)

	# make supplier quotations
	if can_make("Supplier Quotation"):
		from erpnext.stock.doctype.material_request.material_request import make_supplier_quotation

		report = "Material Requests for which Supplier Quotations are not created"
		for row in query_report.run(report)["result"][:how_many("Supplier Quotation")]:
			if row[0] != "'Total'":
				sq = frappe.get_doc(make_supplier_quotation(row[0]))
				sq.transaction_date = current_date
				sq.supplier = supplier
				sq.currency = party_account_currency or company_currency
				sq.conversion_rate = exchange_rate
				sq.insert()
				sq.submit()
				frappe.db.commit()

	# make purchase orders
	if can_make("Purchase Order"):
		from erpnext.stock.doctype.material_request.material_request import make_purchase_order
		report = "Requested Items To Be Ordered"
		for row in query_report.run(report)["result"][:how_many("Purchase Order")]:
			if row[0] != "'Total'":
				po = frappe.get_doc(make_purchase_order(row[0]))
				po.supplier = supplier
				po.currency = party_account_currency or company_currency
				po.conversion_rate = exchange_rate
				po.transaction_date = current_date
				po.insert()
				po.submit()
				frappe.db.commit()

	if can_make("Subcontract"):
		make_subcontract(current_date)


def make_material_request(current_date, item_code, qty):
	mr = frappe.new_doc("Material Request")
	mr.material_request_type = "Purchase"
	mr.transaction_date = current_date
	mr.append("items", {
		"doctype": "Material Request Item",
		"schedule_date": frappe.utils.add_days(current_date, 7),
		"item_code": item_code,
		"qty": qty
	})
	mr.insert()
	mr.submit()


def make_subcontract(current_date):
	from erpnext.buying.doctype.purchase_order.purchase_order import make_stock_entry

	# make sub-contract PO
	po = frappe.new_doc("Purchase Order")
	po.is_subcontracted = "Yes"
	po.supplier = get_random("Supplier")

	po.append("items", {
		"item_code": get_random("Item", {"is_sub_contracted_item": 1}),
		"schedule_date": frappe.utils.add_days(current_date, 7),
		"qty": 20
	})
	po.set_missing_values()
	try:
		po.insert()
	except InvalidCurrency:
		return

	po.submit()

	# make material request for
	make_material_request(current_date, po.items[0].item_code, po.items[0].qty)

	# transfer material for sub-contract
	stock_entry = frappe.get_doc(make_stock_entry(po.name, po.items[0].item_code))
	stock_entry.from_warehouse = "Stores - WP"
	stock_entry.to_warehouse = "Supplier - WP"
	stock_entry.insert()

