from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class GoogleCalendarEvent:
    id: Optional[str]
    summary: Optional[str]
    description: Optional[str]
    start: Dict[str, str]
    end: Dict[str, str]
    location: Optional[str] = None
    status: Optional[str] = None
    htmlLink: Optional[str] = None

    @staticmethod
    def from_google_dict(data: Dict[str, Any]) -> 'GoogleCalendarEvent':
        return GoogleCalendarEvent(
            id=data.get('id'),
            summary=data.get('summary'),
            description=data.get('description'),
            start=data.get('start', {}),
            end=data.get('end', {}),
            location=data.get('location'),
            status=data.get('status'),
            htmlLink=data.get('htmlLink')
        )

    def to_google_dict(self) -> Dict[str, Any]:
        return {
            'summary': self.summary,
            'description': self.description,
            'start': self.start,
            'end': self.end,
            'location': self.location,
            'status': self.status
        }