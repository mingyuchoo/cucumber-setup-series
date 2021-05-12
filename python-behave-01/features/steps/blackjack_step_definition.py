# file: features/steps/blackjack_step_definition.py
# -----------------------------------------------------------------------------
# STEPS:
# -----------------------------------------------------------------------------
from behave import *

from blackjack import Dealer

use_step_matcher("parse")


@given("a dealer")
def step_impl(context):
    context.dealer = Dealer()


@given("a hand {total:d}")
def step_impl(context, total):
    context.dealer = Dealer()
    context.total = total


@given("a {hand}")
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')


@when("the round starts")
def step_impl(context):
    context.dealer.new_round()


@when("the dealer sums the cards")
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()


@when("the dealer determines a play")
def step_impl(context):
    context.dealer_play = context.dealer.determine_play(context.total)


@then("the dealer gives itself two cards")
def step_impl(context):
    assert (len(context.dealer.hand) == 2)


@then("the {total:d} is correct")
def step_impl(context, total):
    assert (context.dealer_total == total)


@then("the {play} is correct")
def step_impl(context, play):
    assert (context.dealer_play == play)


@then("the dealer chooses a play")
def step_impl(context):
    assert (context.dealer.make_play() in ['stand', 'hit'])
