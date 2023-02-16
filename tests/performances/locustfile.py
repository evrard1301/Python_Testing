from locust import HttpUser, task


class GetCompetitionList(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def summary(self):
        self.client.post('/showSummary', {
            'email': 'admin@irontemple.com'
        })
