import json
from django.core.serializers.json import DjangoJSONEncoder
from tastypie.serializers import Serializer
import sys

class ConceptJSONSerializer(Serializer):
    def to_json(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)

#         json_data = {}# = self.to_simple(data, options)
#         json_data["label"]=data.
        # Add in the current time.
#         data['requested_time'] = time.time()
        sys.stderr.write(str(data)+"\n")
        return json.dumps(data, cls=DjangoJSONEncoder, sort_keys=True)

    def from_json(self, content):
        data = json.loads(content)

#         if 'requested_time' in data:
#             # Log the request here...
#             pass

        return data
    
class LinkJSONSerializer(Serializer):
    def to_json(self, data, options=None):
        options = options or {}

        data = self.to_simple(data, options)

        # Add in the current time.
#         data['requested_time'] = time.time()

        return json.dumps(data, cls=DjangoJSONEncoder, sort_keys=True)

    def from_json(self, content):
        data = json.loads(content)

        if 'requested_time' in data:
            # Log the request here...
            pass

        return data