import frappe


@frappe.whitelist(allow_guest=True)
def register(organization_name: str, organization_id: str, organization_email: str, password: str):
	try:
		organization_exists = frappe.db.exists("User", {"username": organization_id})
		if organization_exists:
			frappe.throw("Organization is already taken")
		organization_doc = frappe.get_doc(
			{
				"doctype": "User",
				"username": organization_name,
				"email": organization_email,
				"full_name": organization_name,
				"first_name": organization_name,
			}
		).insert(ignore_permissions=True)
		from frappe.utils.password import update_password

		update_password(organization_id, password)
		organization_doc.add_roles("Organization")

	except Exception:
		frappe.throw("An exception occurred")


@frappe.whitelist(allow_guest=True)
def login(organization_id: str, password: str):
	try:
		organization_exists = frappe.db.exists("User", {"username": organization_id})
		if not organization_exists:
			frappe.throw("Organization does not exist")

		from frappe.utils.password import check_password

		check_password(organization_id, password)
		organization = frappe.db.get_value("User", {"username": organization_id}, "name")

		from frappe.auth import LoginManager

		login_manager = LoginManager()
		login_manager.login_as(organization)

	except frappe.AuthenticationError:
		frappe.throw("Authentication error")


@frappe.whitelist()
def submit_proposal():
	pass
