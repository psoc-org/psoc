import frappe


@frappe.whitelist(allow_guest=True)
def register_and_login(first_name: str, last_name: str | None, username: str, email: str, password: str):
	try:
		mentor_exists = frappe.db.exists("User", {"username": username})
		if mentor_exists:
			frappe.throw("Username is already taken")
		full_name = f"{first_name} {last_name}"
		mentor_doc = frappe.get_doc(
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
		mentor_doc.add_roles("SoC Admin")
		login(username, password)
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
def submit_details(about: str, domain: str, technologies: str, website_url: str, linkedin: str, github: str):
	mentor = frappe.session.user
	roles = frappe.get_roles(mentor)

	allowed = False
	for role in roles:
		if role == "Mentor":
			mentor_details_doc = frappe.get_doc(
				{
					"doctype": "Mentor",
					"mentor": mentor,
					"about": about,
					"domain": domain,
					"technologies": technologies,
					"website": website_url,
					"linkedin": linkedin,
					"github": github,
				}
			)
			mentor_details_doc.insert(ignore_permissions=True)
			mentor_details_doc.add_roles("Mentor")
			allowed = True
	if not allowed:
		frappe.throw("Cannot submit details. Please login.")


@frappe.whitelist()
def get_approved_contributors():
	pass
