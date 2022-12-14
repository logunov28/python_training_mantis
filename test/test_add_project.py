from model.project import Project

def test_add_project(app):
    app.open_home_page()
    app.session.login("administrator", "root")
    old_projects = app.soap.get_projects_list()
    if old_projects is None:
        old_projects = []
    project = Project(name="First_project", status='development', view_status='public', description='text')
    app.project.create(project)
    app.project.return_to_projects_page()
    new_projects = app.soap.get_projects_list()
    assert len(old_projects)+1 == len(new_projects)
    old_projects.append(project)
    #assert str(old_projects) == str(new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

