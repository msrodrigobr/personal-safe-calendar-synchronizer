from typing import Set, Dict
from personal_safe_calendar_synchronizer.model import CalendarEvent, GoogleCalendarEvent
from personal_safe_calendar_synchronizer.calendar.google.google_calendar_service import GoogleCalendarService

class CalendarSyncService:
    def __init__(self, calendar_id: str, google_calendar_service: GoogleCalendarService):        
        self.cached_calendar_events: Set[CalendarEvent] = set()
        self.map_calendar_events: Dict[CalendarEvent, GoogleCalendarEvent]
        self.calendar_id = calendar_id
        self.google_calendar_service = google_calendar_service
    
    def sync_events(self, events: Set[CalendarEvent]):        
        events_to_remove = self.cached_calendar_events - events
        for event in events:
            if event not in self.cached_calendar_events:
                google_event = self.google_calendar_service.insert_event(calendar_id=self.calendar_id, event=event)
                self.cached_calendar_events.add(event)
                self.map_calendar_events[event] = google_event

        for event in events_to_remove:
            google_event = self.map_calendar_events.get(event)
            if google_event:
                self.google_calendar_service.delete_event(calendar_id=self.calendar_id, event=google_event)
                del self.map_calendar_events[event]
                self.cached_calendar_events.remove(event)