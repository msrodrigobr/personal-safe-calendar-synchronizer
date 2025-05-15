from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class CalendarEvent:
    """
    Represents a calendar event.
    """
    subject: str
    start_time: Dict[str, str]
    end_time: Dict[str, str]
    show_as: str
    is_all_day: bool
    organizer: Any

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'CalendarEvent':
        """
        Create a CalendarEvent instance from a dictionary.
        """
        return CalendarEvent(
            subject=data.get('subject', ''),
            start_time=data.get('start_time', {}),
            end_time=data.get('end_time', {}),
            show_as=data.get('show_as', ''),
            is_all_day=data.get('is_all_day', False),
            organizer=data.get('organizer', None)
        )

