
class Project:

    def __init__(self, name=None, status='development', inherit=True, view_status='public', description=None, index=None):
        self.name = name
        self.status = status
        self.inherit = inherit
        self.view_status = view_status
        self.description = description
        self.index = index

    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.name, self.status, self.inherit, self.view_status, self.description)


"""
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
"""