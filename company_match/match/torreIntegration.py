import requests

class TorreIntegration():
    def __init__(self):
        self.url = "https://torre.bio/api/"
        self.endpoint_bio = "bios/"

    def get_bio(self, username):
        bio_url = "{}{}{}".format(self.url, self.endpoint_bio, username)
        return requests.get(bio_url)