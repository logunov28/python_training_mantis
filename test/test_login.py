def test_login(app):
    app.session.login(app.username, app.password)
    assert app.session.is_logged_in_as("administrator")
