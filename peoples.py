class People:

    def __init__(self):
        self.name = ""
        self.first_name = ""
        self.middle_name = ""
        self.last_name = ""

        self.date_of_birth = None

        self.address = []
        self.social_mdeia = []

        self.images = []


class SocialMedia:

    def __init__(self):
        self.name = ""
        self.url = ""
        self.username = ""
        self.id = ""

        self.last_check_date = None


class Images:

    def __init__(self):
        self.path = ""
        self.alt = ""