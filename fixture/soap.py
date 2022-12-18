from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(self.app.username, self.app.password)
            projects_list = []
            for i in projects:
                projects_list.append(Project(name=i["name"], status=i['status']['name'], view_status=i['view_state']['name'], description=i['description']))
            return projects_list
        except WebFault:
            return False