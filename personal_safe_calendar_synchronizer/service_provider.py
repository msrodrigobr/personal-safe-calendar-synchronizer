from personal_safe_calendar_synchronizer.config import Config
from personal_safe_calendar_synchronizer.calendar.calendar_sync_service import CalendarSyncService
from personal_safe_calendar_synchronizer.calendar.google.google_calendar_service import GoogleCalendarService
from google.oauth2.service_account import Credentials

class ServiceProvider:
    _instance = None

    def __init__(self, config: Config):
        self.config = config
        self.google_credentials = Credentials.from_service_account_file( 
            self.config.google_crendentials_path,
            scopes=['https://www.googleapis.com/auth/calendar']
        )
        self.calendar_sync_service = CalendarSyncService(self.config.calendar_to_sync, GoogleCalendarService(self.google_credentials))

    def get_calendar_sync_service(self) -> CalendarSyncService:
        return self.calendar_sync_service
