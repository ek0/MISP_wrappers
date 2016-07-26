#!/usr/bin/env python2

# Author: Jessy Campos

import sys
from keys import misp_key, misp_url, pymisp_path
sys.path.append(pymisp_path)
from pymisp import PyMISP

def push_hash(misp_instance, event_id, filename, md5, sha1, sha256, comment=None):
    tmp = misp_instance.get_event(event_id)
    event = tmp.json()
    return misp_instance.add_hashes(event, "Payload installation", filename, md5, sha1, sha256, comment=comment)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Push a filename and its hashes to an existing event")
    parser.add_argument("-e", "--event", required=True, help="Event ID")
    parser.add_argument("-f", "--filename", required=False, help="Filename")
    parser.add_argument("--md5", required=False, help="MD5 of the sample")
    parser.add_argument("--sha1", required=False, help="SHA1 of the sample")
    parser.add_argument("--sha256", required=False, help="SHA256 of the sample")
    parser.add_argument("--comment", required=False, help="Some comment to add")
    
    args = parser.parse_args()

    misp = PyMISP(misp_url, misp_key, True, 'json')

    push_hash(misp, args.event, args.filename, args.md5, args.sha1, args.sha256, comment=args.comment)
