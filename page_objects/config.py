class Config:
    def __init__(self, env):
        self.base_url = {
            'dev': 'ausweis.io',
            'prod': 'https://my.ausweis.io/ru/accounts/login/'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]
