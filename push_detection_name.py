#!/usr/bin/env python2

# Author: Jessy Campos

import sys
from keys import misp_key, misp_url, pymisp_path
sys.path.append(pymisp_path)
from pymisp import PyMISP

def push_detection_name(misp_instance, event_id, detection_name):
    tmp = misp_instance.get_event(event_id)
    event = tmp.json()
    return misp_instance.add_detection_name(event, detection_name)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Push a filename to a remote MISP instance.")
    parser.add_argument("-e", "--event", required=True, help="Event ID")
    parser.add_argument("-d", "--detection", required=True, help="Detection name to add")
    
    args = parser.parse_args()

    misp = PyMISP(misp_url, misp_key, True, 'json')

    push_detection_name(misp, args.event, args.detection)
