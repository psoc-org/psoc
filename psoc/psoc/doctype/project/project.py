# Copyright (c) 2025, Team PSoC and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Project(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		desc: DF.Data
		github: DF.Data
		location: DF.Data
		org_id: DF.Data
		pro_name: DF.Data
	# end: auto-generated types

	pass
