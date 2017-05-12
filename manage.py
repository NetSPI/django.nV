#!/usr/bin/env python

#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#			INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskManager.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
