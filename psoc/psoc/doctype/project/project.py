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

		description: DF.LongText
		github: DF.Data
		organization: DF.Link
		project_name: DF.Data
		technologies: DF.Data
	# end: auto-generated types

	pass
