import requests
class OpenAgendaService:
    def __init__(self):
        self.root = "https://api.openagenda.com/v2/agendas"
        self.public_key = "oa_pk_UUNnLgkZfepGYZDPjLAsAaStzJMbvytGPawMoaunCqsyBIUzVhgSVzekzyqapvmN"

    def fetch_events(self,agenda,start_date:str|None= None ,
                     end_date:str|None= None,
                     location: tuple[float,float]| None = None
                     )-> dict:

        url = f"{self.root}/{agenda}/events"
        params = {'key': self.public_key}

        # Paramètres optionnels
        if start_date is not None:
            params["timings[gte]"] = start_date
        if end_date is not None:
            params["timings[lte]"] = end_date


        res = requests.get(url, params=params)
        res.raise_for_status()
        return res.json()


