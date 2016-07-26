#!/usr/bin/env python2

# Author: Jessy Campos

import sys
from keys import misp_key, misp_url, pymisp_path
sys.path.append(pymisp_path)
from pymisp import PyMISP

def push_regkey(misp_instance, event_id, regkey, rvalue=None):
    tmp = misp_instance.get_event(event_id)
    event = tmp.json()
    return misp_instance.add_regkey(event, regkey, rvalue, "Artifacts dropped")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Push a registry key path to a remote MISP instance.")
    parser.add_argument("-e", "--event", required=True, help="Event ID")
    parser.add_argument("--regkey", required=True, help="Registry key to push.")
    parser.add_argument("--value", required=False, help="Registry key value.")
    
    args = parser.parse_args()

    misp = PyMISP(misp_url, misp_key, True, 'json')

    push_regkey(misp, args.event, args.regkey, args.value)
