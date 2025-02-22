# Copyright (c) 2025, Team PSoC and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class OrganizationProposal(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		execution_plan: DF.TextEditor
		mentoring_plan: DF.LongText
		organization: DF.Link
		projects: DF.TextEditor
		reason: DF.LongText
		status: DF.Literal["Pending", "Accepted", "Rejected"]
		support_from_soc: DF.LongText
	# end: auto-generated types
