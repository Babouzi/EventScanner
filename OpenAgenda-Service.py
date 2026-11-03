import requests
class OpenAgendaService:
    def __init__(self):
        self.root = "https://api.openagenda.com/v2/agendas"
        self.public_key = "oa_pk_UUNnLgkZfepGYZDPjLAsAaStzJMbvytGPawMoaunCqsyBIUzVhgSVzekzyqapvmN"

    def fetch_events(self,agenda,start_date: str,end_date: str,location: tuple[float,float]) -> dict:
        url = f"{self.root}/{agenda}"
        params = {key:self.public_key for key in location}
        req = requests.get(url, params=params).json()
        return req
