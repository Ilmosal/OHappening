"""
This module contains the CalendarManager class for accessing the correct Google Calendar Accounts
"""
import os
from datetime import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from ohappening.event import Event
from ohappening.config import PROJECT_PATH

class CalendarManager():
    """
    Class for managing a single calendar and all calendar operations
    """
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def __init__(self, calendar_config, logger):
        self.logger = logger

        self.logger.info("Setting up calendar {0}".format(calendar_config['name']))

        self.credentials_name = calendar_config['name']
        credentials_file = calendar_config['credentials_file']

        self.pickle_path = os.path.join(PROJECT_PATH, 'credentials/{0}.pickle'.format(self.credentials_name))
        self.credentials_path = os.path.join(PROJECT_PATH, 'credentials/{0}'.format(credentials_file))
        self.calendar_names = calendar_config['calendar_names']
        self.calendar_ids = []
        self.working = False

        self.createConnection()

    def createConnection(self):
        """
        Function for building the calendar service 
        """
        try:
            creds = None

            self.logger.info("Reading credentials")
            if os.path.exists(self.pickle_path):
                with open(self.pickle_path, 'rb') as token:
                    creds = pickle.load(token)

            if not creds or not creds.valid:
                self.logger.debug("Credentials not valid! Validating credentials.")

                if creds and creds.expired and creds.refresh_token:
                    self.logger.debug("Refreshing expired credentials")
                    creds.refresh(Request())
                else:
                    self.logger.info("Problem with credentials! Try to refresh credentials again in browser!!")

                    flow = InstalledAppFlow.from_client_secrets_file(
                           self.credentials_path, self.SCOPES)
                    creds = flow.run_local_server(port=0)
                with open(self.pickle_path, 'wb') as token:
                    self.logger.debug("Dumping the pickle for calendar {0}".format(self.credentials_name))
                    pickle.dump(creds, token)

            self.logger.info('Building calendar service')
            self.service = build('calendar', 'v3', credentials=creds)

            self.logger.info("Fetching calendar ids")
            calendar_id_results = self.service.calendarList().list().execute()

            self.calendar_ids = []

            for result in calendar_id_results.get('items', []):
                self.logger.debug(result)
                if result.get('summary') in self.calendar_names:
                    self.calendar_ids.append(result.get('id'))

            self.working = True

        except Exception as e:
            self.logger.info("Exception occurred while building the calendar service {0}".format(self.credentials_name))
            self.logger.info("Exception: {0}".format(e))
            self.working = False

    def fetchEvents(self):
        """
        Function for fetching next 10 upcoming events from this CalendarManager
        """
        if not self.working:
            self.createConnection()

        self.logger.info('Fetching new events from calendar {0}'.format(self.credentials_name))

        events = []
        now = datetime.utcnow().isoformat() + 'Z'

        try:
            for calendar_id in self.calendar_ids:
                self.logger.debug('Fetching all events for calendar_id {0}'.format(calendar_id))
                events_result = self.service.events().list(
                        calendarId=calendar_id,
                        timeMin=now,
                        maxResults=10,
                        singleEvents=True,
                        orderBy='startTime').execute()

                json_events = events_result.get('items', [])

                for json_e in json_events:
                    self.logger.debug('Creating new event from json: \n{0}'.format(json_e))

                    try:
                        start_time = datetime.strptime(json_e['start'].get('dateTime', json_e['start'].get('date')).split('+')[0], '%Y-%m-%dT%H:%M:%S')
                    except:
                        start_time = datetime.strptime(json_e['start'].get('dateTime', json_e['start'].get('date')).split('+')[0], '%Y-%m-%d')

                    try:
                        end_time = datetime.strptime(json_e['end'].get('dateTime', json_e['end'].get('date')).split('+')[0], '%Y-%m-%dT%H:%M:%S')
                    except:
                        end_time = datetime.strptime(json_e['end'].get('dateTime', json_e['end'].get('date')).split('+')[0], '%Y-%m-%d')

                    events.append(Event(
                        json_e.get('summary'),
                        json_e.get('location'),
                        self.credentials_name,
                        json_e.get('description'),
                        start_time,
                        end_time
                        ))

        except Exception as e:
            self.logger.info("Exception occurred while fetching events {0}".format(self.credentials_name))
            self.logger.info("Exception: {0}".format(e))
            self.working = False

        return events

