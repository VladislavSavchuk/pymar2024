""" Module for locator storage """


class EditContactLocators:
    """ The class contains locators to edit a contact """
    # contact row
    contact_row = '//*[@class="contactTable"]/tr[1]'
    contact_deleted = "//*[contains(text(), '{contact_name}')]"
    # buttons
    edit_contact_btn = '[id="edit-contact"]'
    delete_contact_btn = '[id="delete"]'
    return_to_contacts_btn = '[id="return"]'
    submit_btn = '[id="submit"]'
    cancel_btn = '[id="cancel"]'
    # forms
    first_name_form = '[id="firstName"]'
    last_name_form = '[id="lastName"]'
    birthdate_form = '[id="birthdate"]'
    email_form = '[id="email"]'
    phone_form = '[id="phone"]'
    street1_form = '[id="street1"]'
    street2_form = '[id="street2"]'
    city_form = '[id="city"]'
    state_form = '[id="stateProvince""]'
    postal_code_form = '[id="postalCode"]'
    country_form = '[id="country"]'
