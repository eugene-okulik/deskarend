def test_create_account(create_account, account_page, first_name, last_name, email, password):
    creating_new_account_text = 'Thank you for registering with Main Website Store.'

    create_account.open_page()
    create_account.create_account(first_name, last_name, email, password, password)

    account_page.check_creating_new_account(creating_new_account_text)


def test_fill_incorrect_email(create_account):
    incorrect_email = "Incorrect_email"
    email_error_text = 'Please enter a valid email address (Ex: johndoe@domain.com).'

    create_account.open_page()
    create_account.fill_email(incorrect_email)
    create_account.click_create_account()

    create_account.check_is_there_email_error(email_error_text)


def test_fill_different_passwords(create_account, password):
    a_different_password = 'Another' + password
    confirm_password_error = 'Please enter the same value again.'

    create_account.open_page()
    create_account.fill_password(password)
    create_account.fill_confirm_password(a_different_password)
    create_account.click_create_account()

    create_account.check_is_there_confirm_error(confirm_password_error)
