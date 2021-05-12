# file: features/steps/tutorial_step_definition.py
# -----------------------------------------------------------------------------
# STEPS:
# -----------------------------------------------------------------------------
from behave import *


@given("we have behave installed")
def step_impl(context):
    pass


@when("we implement a test")
def step_impl(context):
    assert True is not False


@then("behave will test it for us!")
def step_impl(context):
    assert False is not True
