from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class CalendarEvent:
    """
    Represents a calendar event.
    """
    id: str
    subject: str
    start_time: dict
    end_time: dict
    show_as: str
    is_all_day: bool
    organizer: dict

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'CalendarEvent':
        """
        Create a CalendarEvent instance from a dictionary.
        """
        return CalendarEvent(
            id=data.get('id', ''),
            subject=data.get('subject', ''),
            start_time=data.get('start_time', {}),
            end_time=data.get('end_time', {}),
            show_as=data.get('show_as', ''),
            is_all_day=data.get('is_all_day', False),
            organizer=data.get('organizer', {})
        )
    
    # __eq__ and __hash__ are based soely on the id
    def __eq__(self, other: 'CalendarEvent') -> bool:
        if not isinstance(other, CalendarEvent):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

