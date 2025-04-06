import sys
import os
from pathlib import Path

# Ajouter le répertoire src au chemin Python pour permettre l'importation des modules
src_path = str(Path(__file__).resolve().parents[3])
if src_path not in sys.path:
    sys.path.append(src_path)

# Importer la fonction download_to_local
try:
    from helpers.dowloader import download_to_local
except ImportError:
    # Fallback si l'importation échoue
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "dowloader", 
        os.path.join(src_path, "helpers", "dowloader.py")
    )
    dowloader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dowloader)
    download_to_local = dowloader.download_to_local

from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand


STATICFILES_VENDORS_DIR = getattr(settings,'STATICFILES_VENDORS_DIR')

VENDOR_STATICFILES = {
    "saas-theme.min.css": "https://raw.githubusercontent.com/codingforentrepreneurs/SaaS-Foundations/main/src/staticfiles/theme/saas-theme.min.css",
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"
}

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")
        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDORS_DIR / name
            dl_success = download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download {url}')
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS('Successfully updated all vendor static files.')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Some files were not updated.')
            )