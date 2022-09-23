import json
import os

BROKER_TRANSPORT_OPTIONS = json.loads(os.getenv('BROKER_TRANSPORT_OPTIONS', '{}'))
