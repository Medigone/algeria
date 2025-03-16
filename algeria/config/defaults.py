import frappe

def get_data():
    return {
        "country": "Algeria",
        "currency": "DZD",
        "date_format": "dd/mm/yyyy",
        "language": "fr"
    }

def apply_defaults():
    data = get_data()

    # Mettre à jour les valeurs globales
    for key, value in data.items():
        frappe.db.set_value("System Settings", None, key, value)

    frappe.db.commit()
