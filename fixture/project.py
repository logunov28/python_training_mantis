from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def return_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        # init group creation
        wd.find_element_by_css_selector("[value='Create New Project']").click()
        # fill group form
        self.fill_project_form(project)
        # submit group creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def delete_first_project(self):
        self.delete_project_by_index(0)

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.return_to_projects_page()
        wd.find_elements_by_css_selector('[href="manage_proj_edit_page"]')[index].click()
        wd.find_element_by_css_selector('[value="Delete Project"]').click()
        wd.find_element_by_css_selector('[value="Delete Project"]').click()

    def delete_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        wd.find_element_by_name("status").click()
        wd.find_element_by_xpath("//option[@value='10']").click()
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_xpath("//tr[5]/td[2]/select/option").click()
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_project(self):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_css_selector('[href="manage_proj_edit_page"]')[0].click()
        wd.find_element_by_css_selector('[value="Delete Project"]').click()
        wd.find_element_by_css_selector('[value="Delete Project"]').click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        return len(wd.find_elements_by_name("selected[]"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            index = 0
            for element in wd.find_elements_by_xpath("//table[3]/tbody/tr")[2:]:
                text = element.find_elements_by_tag_name("td")
                name = text[0].text
                status = text[1].text
                view_status = text[3].text
                description = text[4].text
                self.project_cache.append(Project(name=name, status=status, view_status=view_status, description=description, index=index))
                index += 1
        return list(self.project_cache)