from model.project import Project
import random


def test_del_project(app):
    app.session.login("administrator", "root")
    old_projects = app.soap.get_projects_list()
    if len(old_projects) == 0:
        project = Project(name="First_project", status="development", view_status="public", description="text")
        app.project.add_project(project)
        old_projects = app.soap.get_projects_list()
    app.project.delete_first_project()
    project = random.choice(old_projects)
    new_projects = app.soap.get_projects_list()
    old_projects.remove(project)
    app.session.logout()
    assert old_projects == new_projects
