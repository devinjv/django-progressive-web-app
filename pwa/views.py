from django.shortcuts import render

from . import app_settings


def service_worker(request):
    response = render(request, app_settings.PWA_SERVICE_WORKER_PATH, content_type='application/javascript')
    return response


def manifest(request):
    return render(request, 'manifest.json', {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('PWA_')
    })
