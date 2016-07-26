#!/usr/bin/env python2

# Author: Jessy Campos

import sys
from keys import misp_key, misp_url, pymisp_path
sys.path.append(pymisp_path)
from pymisp import PyMISP

def push_mutex(misp_instance, event_id, mutex):
    tmp = misp_instance.get_event(event_id)
    event = tmp.json()
    return misp_instance.add_mutex(event, mutex, "Artifacts dropped")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Push a mutex name to a remote MISP instance.")
    parser.add_argument("-e", "--event", required=True, help="Event ID")
    parser.add_argument("--mutex", required=True, help="Mutex to push.")
    
    args = parser.parse_args()

    misp = PyMISP(misp_url, misp_key, True, 'json')

    push_mutex(misp, args.event, args.mutex)
