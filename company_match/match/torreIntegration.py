import requests

class TorreIntegration():
    def __init__(self):
        self.endpoint_bio = "https://torre.bio/api/bios/"
        self.endpoint_jobs = "https://search.torre.co/opportunities/_search/"
        self.headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        }

    def get_bio(self, username):
        bio_url = "{}{}".format(self.endpoint_bio, username)
        return requests.get(bio_url)

    def get_dream_jobs(self, **kwargs):
        response = requests.post(self.endpoint_jobs, headers=self.headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return []
        return response.json()
