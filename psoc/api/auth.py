import frappe


@frappe.whitelist(allow_guest=True)
def login(email: str, password: str):
	try:
		user_exists = frappe.db.exists("User", {"email": email})
		if not user_exists:
			frappe.throw("User does not exist")

		from frappe.utils.password import check_password

		username = frappe.db.get_value("User", {"email": email}, "username")
		check_password(username, password)
		user = frappe.db.get_value("User", {"username": username}, "name")

		from frappe.auth import LoginManager

		login_manager = LoginManager()
		login_manager.login_as(user)

	except frappe.AuthenticationError:
		frappe.throw("Authentication error")
