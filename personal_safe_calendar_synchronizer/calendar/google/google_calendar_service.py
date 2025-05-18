from datetime import datetime, timedelta, timezone, time
from googleapiclient.discovery import build
from personal_safe_calendar_synchronizer.model import CalendarEvent, GoogleCalendarEvent

class GoogleCalendarService:
    def __init__(self, credentials):
        self.credentials = credentials
        self.service = self.create_service()

    def create_service(self):
        return build('calendar', 'v3', credentials=self.credentials)

    def list_events(self, calendar_id, max_results=10):
        now = datetime.combine(datetime.now(tz=timezone.utc), time(0, 0, 0))
        print(now, flush=True)
        start_of_week = now - timedelta(days=now.weekday())
        print(start_of_week, flush=True)
        end_of_week = start_of_week + timedelta(days=7)
        print(end_of_week, flush=True)

        events_result = self.service.events().list(
            calendarId=calendar_id,
            timeMin=start_of_week.isoformat() + 'Z',
            timeMax=end_of_week.isoformat() + 'Z',
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        return events_result.get('items', [])

    def insert_event(service, calendar_id: str, event: CalendarEvent) -> GoogleCalendarEvent:
        event_body = {
            'summary': event.subject,
            'start': {
                'dateTime': event.start_time['dateTime'],
                'timeZone': event.start_time.get('timeZone', 'UTC'),
            },
            'end': {
                'dateTime': event.end_time['dateTime'],
                'timeZone': event.end_time.get('timeZone', 'UTC'),
            },
            'description': f"Organized by {event.organizer}",
            'transparency': 'opaque' if event.show_as.lower() == 'busy' else 'transparent',
        }
        result = service.events().insert(calendarId=calendar_id, body=event_body).execute()
        return GoogleCalendarEvent.from_google_dict(result)

    def delete_event(service, calendar_id: str, event_id: str):
        service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
