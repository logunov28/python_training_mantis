from sys import maxsize

class Project:

    def __init__(self, name=None, status='development', inherit=True, view_status='public', description=None, index=None, id=None):
        self.name = name
        self.status = status
        self.inherit = inherit
        self.view_status = view_status
        self.description = description
        self.index = index
        self.id = id

    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.name, self.status, self.inherit, self.view_status, self.description)


    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name) \
               and (self.status is None or other.status is None or self.status == other.status) \
               and (self.view_status is None or other.view_status is None or self.view_status == other.view_status) \
               and (self.description is None or other.description is None or self.description == other.description)\
               and (self.index is None or other.index is None or self.index == other.index)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize