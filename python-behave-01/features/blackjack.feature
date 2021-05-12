@FEATURE-0001
Feature: The dealer for Blackjack

  @SPEC-0001
  Scenario: Deal initial cards
    Given a dealer
    When the round starts
    Then the dealer gives itself two cards


  @SPEC-0002
  Scenario Outline: Get hand total
    Given a <hand>
    When the dealer sums the cards
    Then the <total> is correct

    Examples: Hands
      | hand  | total |
      | 5,7   | 12    |
      | 5,Q   | 15    |
      | Q,Q,A | 21    |
      | Q,A   | 21    |
      | A,A,A | 13    |


  @SPEC-0003
  Scenario Outline: Dealer plays by the rules
    Given a hand <total>
    When the dealer determines a play
    Then the <play> is correct

    Examples: Hands
      | total | play  |
      | 10    | hit   |
      | 15    | hit   |
      | 16    | hit   |
      | 17    | stand |
      | 18    | stand |
      | 19    | stand |
      | 20    | stand |
      | 21    | stand |
      | 22    | stand |


  @SPEC-0004
  Scenario: A Dealer can always play
    Given a dealer
    When the round starts
    Then the dealer chooses a play
