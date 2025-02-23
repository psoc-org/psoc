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
		)

		mentor_doc.save(ignore_permissions=True)
		mentor_doc.insert(ignore_permissions=True)
		mentor_doc.add_roles("Mentor")

		from frappe.utils.password import update_password

		update_password(username, password)

		login(username, password)

		frappe.db.commit()

		return {"status": "success", "role": "Contributor"}

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


@frappe.whitelist(allow_guest=True)
def submit_details(about: str, domain: str, technologies: str, website_url: str, linkedin: str, github: str):
	mentor = frappe.session.user

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

	user_permission = frappe.new_doc("User Permission")
	user_permission.user = mentor
	user_permission.allow = "Mentor"
	user_permission.for_value = mentor_details_doc

	user_permission.insert(ignore_permissions=True)
	frappe.db.commit()


@frappe.whitelist(allow_guest=True)
def get_mentor_profile(contributor_id: str):
	try:
		# Fetch a specific contributor profile based on ID
		contributor = frappe.get_all(
			"Contributor",
			filters={"name": contributor_id},
			fields=["about", "contributor", "linkedin", "github", "resume"],
		)
		if not contributor:
			return {"status": "error", "message": "Contributor not found"}

		return {"status": "success", "data": contributor}
	except Exception as e:
		frappe.log_error(frappe.get_traceback(), "get_contributor_profile Error")
		return {"status": "error", "message": str(e)}


@frappe.whitelist()
def get_approved_contributors():
	pass
