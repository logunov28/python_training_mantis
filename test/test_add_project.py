from model.project import Project

def test_add_project(app):
    app.open_home_page()
    app.session.login("administrator", "root")
    old_projects = app.soap.get_projects_list()
    project = Project(name="First_project", status='development', view_status='public', description='text')
    app.project.create(project)
    app.project.return_to_projects_page()
    new_projects = app.soap.get_projects_list()
    assert sorted(old_projects) == sorted(new_projects)

