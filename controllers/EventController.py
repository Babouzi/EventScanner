from services.OpenAgendaService import OpenAgendaService
from models.models import Event

class EventController:
    def __init__(self):
        self.api_service = OpenAgendaService()



    def process_agenda(self, agenda_id: str) -> list:
        #Appel du service
        liste_event = self.api_service.fetch_events(agenda_id)
        parsed_events =[]

        for event in liste_event["events"]:
            #Formatage des events par pydantic
            current_event = Event(title=event.get("title","Sans titre"),
                                  description=event.get("description","Sans description"),
                                  start_time=event.get("start_time","Sans date de début"),
                                  end_time=event.get("end_time","Sans date de fin"),
                                  url = event.get("url","")
                                  )
            parsed_events.append(current_event)

        return parsed_events




