import json
import os
from flask import Flask, request, jsonify
from personal_safe_calendar_synchronizer.decrypt import decrypt_json_simple
from personal_safe_calendar_synchronizer.model import CalendarEvent
from personal_safe_calendar_synchronizer.service_provider import ServiceProvider
from .config import Config


config = Config.load()
service_provider = ServiceProvider(config)

app = Flask(__name__)
@app.route('/', methods=['POST'])
def create_calendar_event():
    data = request.get_json()
    events_json = None
    if not config.disable_encryption:
        events_json = decrypt_json_simple(data, "cetao")
    else:
        events_json = json.loads(data)
    events = [CalendarEvent.from_dict(event) for event in events_json]
    service_provider.get_calendar_sync_service().sync_events(events)
    return jsonify({"message": "Accepted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
