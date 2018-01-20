import json

from behave import when, then, given
from behave_django.decorators import fixtures

from services import services


@given('there is an empty ServiceRegistry')
def empty_service_registry(context):
    pass


@when('I add a service "{service}" with version "{version}"')
def create_service(context, service, version):
    context.response = context.test.client.post(
        context.get_url('services:add'), {'type': service, 'version': version}
    )


@fixtures('services-data.json')
@when('I update a service')
def update_service(context):
    context.response = context.test.client.patch(
        context.get_url('services:update', pk=1),
        data={'version': '0.0.2'},
        content_type='application/x-www-form-urlencoded'
    )


@fixtures('services-data.json')
@when('I search for a service "{service}" with version "{version}"')
def search_service(context, service, version):
    context.response = context.test.client.get(
        context.get_url('services:list'), {'type': service, 'version': version}
    )


@fixtures('services-data.json')
@when('I search for a service "{service}" without version')
def search_for_service_without_version(context, service):
    context.response = context.test.client.get(
        context.get_url('services:list'), {'type': service}
    )


@fixtures('services-data.json')
@when('I remove a service')
def remove_service(context):
    context.response = context.test.client.delete(context.get_url('services:delete', pk=1))


@then('I should be notified with a change "{changed}"')
def created_notification(context, changed):
    context.test.assertEqual(context.response.message, changed)


@then('I should find count "{count}" instances of service')
def services_count(context, count):
    response = json.loads(context.response.content.decode())
    context.test.assertEqual(len(response), int(count))


@then('the service "{service}" should have the correct type')
def check_service_type(context, service):
    response = json.loads(context.response.content.decode()).pop()
    context.test.assertEqual(response.get('type'), service)


@then('the service "{service}" should have the correct version "{version}"')
def check_service_type(context, service, version):
    response = json.loads(context.response.content.decode()).pop()
    context.test.assertEqual(response.get('version'), version)


@then('I should find count "{count}" services')
def search_non_existing_services(context, count):
    response = json.loads(context.response.content.decode())
    context.test.assertEqual(len(response), int(count))


@then('the service should be removed')
def check_deleted_service(context):
    context.test.assertIsNone(services.get_service(pk=1))
