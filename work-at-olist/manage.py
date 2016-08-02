#!/usr/bin/env python
import os
import sys
from prettyconf import config

if __name__ == "__main__":
    settings = config('SETTINGS', default='workatolist.settings.local')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
