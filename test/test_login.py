from pom.login import Login


def test_valid_username_password(driver):
    login = Login(driver)
    login.login_with_cred("dan@gmail.com", "test1234")
