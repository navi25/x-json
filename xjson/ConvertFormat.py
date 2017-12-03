import json
import xml.etree.ElementTree as ET
from xjson.xmlcsv import convert_from_xml
from xjson.jsoncsv import convert_from_json
from xjson.Constants import UpdatePath
from xjson.xmlcsv import get_file_name

def convert_uploaded_file(f):
    #filename = get_file_name(f)
    #UpdatePath(filename)
    #print("convert_uploaded_file - ", filename)
    filename = f.name
    if filename.endswith(".xml"):
        return convert_from_xml(f)

    if filename.endswith(".json"):
        return convert_from_json(f)

