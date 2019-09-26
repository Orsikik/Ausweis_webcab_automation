class Config:
    def __init__(self, env):
        self.base_url = {
            'dev': 'https://www.ausweis.io/en/',
            'prod': 'https://my.ausweis.io/ru/accounts/login/'
        }[env]

        self.app_port = {
            'dev': 8080,
            'prod': 80
        }[env]
