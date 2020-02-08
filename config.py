# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'indianapolis',
    package_name = 'montclair-indianapolis',
    name = 'Go Indianapolis',
    description = 'Real Time Tracking of the Buses for Indianapolis, IN',
    url = 'https://indianapolis.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.6.2',
        revision = 1,
        title = 'Go Indianapolis',
        first_run_text = "Welcome to Indianapolis, IN's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 1,
        app_id = 'com.gotransitapp.indianapolis',
        app_store_id = '1493867700',
        app_store_url = 'https://apps.apple.com/us/app/go-indianapolis/id1493867700'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.indianapolis',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.indianapolis'
    )
)
