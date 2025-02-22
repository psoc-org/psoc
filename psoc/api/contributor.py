import frappe


@frappe.whitelist(allow_guest=True)
def register(first_name: str, last_name: str | None, username: str, email: str, password: str):
	try:
		contributor_exists = frappe.db.exists("User", {"username": username})
		if contributor_exists:
			frappe.throw("Username is already taken")
		full_name = f"{first_name} {last_name}"
		contributor_doc = frappe.get_doc(
			{
				"doctype": "User",
				"username": username,
				"email": email,
				"first_name": first_name,
				"last_name": last_name,
				"full_name": full_name,
			}
		).insert(ignore_permissions=True)
		from frappe.utils.password import update_password

		update_password(username, password)
		contributor_doc.add_roles("Contributor")
	except Exception:
		frappe.throw("An exception occurred")


@frappe.whitelist(allow_guest=True)
def login(username: str, password: str):
	try:
		user_exists = frappe.db.exists("User", {"username": username})
		if not user_exists:
			frappe.throw("User does not exist")

		from frappe.utils.password import check_password

		check_password(username, password)
		user = frappe.db.get_value("User", {"username": username}, "name")

		from frappe.auth import LoginManager

		login_manager = LoginManager()
		login_manager.login_as(user)

	except frappe.AuthenticationError:
		frappe.throw("Authentication error")


@frappe.whitelist()
def submit_proposal():
	pass
