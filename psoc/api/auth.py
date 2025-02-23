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
		user = frappe.db.get_value(
			"User", {"username": username}, fieldname=["name", "username"], as_dict=True
		)

		from frappe.auth import LoginManager

		login_manager = LoginManager()
		login_manager.login_as(user.get("name"))
		role = "Guest"
		roles = frappe.get_roles(user.get("username"))
		for r in roles:
			match r:
				case "Contributor":
					role = "Contributor"
					break
				case "SoC Admin":
					role = "SoC Admin"
					break
				case "Mentor":
					role = "Mentor"
					break
				case "Organizer":
					role = "Organizer"
					break

		return {"status": "success", "role": role}

	except frappe.AuthenticationError:
		frappe.throw("Authentication error")
