#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomeSite.settings.dev")

    from django.core.management import django

    django(sys.argv)
    
