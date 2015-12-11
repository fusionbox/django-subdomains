from django.conf import settings

if not settings.configured:
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.sites',
            'subdomains',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            },
        },
        SITE_ID=1,
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'subdomains.middleware.SubdomainURLRoutingMiddleware',
        ),
    )




def run():
    import sys

    from django.test.utils import get_runner
    try:
        from django import setup
    except ImportError:
        # Django < 1.7
        pass
    else:
        setup()

    from subdomains.tests.tests import *  # NOQA
    runner = get_runner(settings)()
    failures = runner.run_tests(('subdomains',))
    sys.exit(failures)
