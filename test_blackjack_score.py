from main import blackjack_score
import pytest


# @pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
    # Arrange
    hand = [3, 4]
    expected_result = 7

    # Act
    score = blackjack_score(hand)

    # Assert <-- Write assert statement here
    assert score == expected_result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
    # Arrange
    hand = [3, 4, "Jack"]
    expected_result = 17

    # Act
    score = blackjack_score(hand)

    # Assert
    assert score == expected_result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
    hand = [3, 4, "Ace"]
    expected_result = 18

    # Act
    score = blackjack_score(hand)

    # Assert
    assert score == expected_result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():

    hand = [3, 8, "Ace"]
    expected_result = 12

    # Act
    score = blackjack_score(hand)

    # Assert
    assert score == expected_result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
    hand = [3]
    expected_result = "Invalid cards"

    # Act
    score = blackjack_score(hand)

    # Assert
    assert score == expected_result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():

    hand = [3, 4, 5, "Jack", "Queen", "King", "Ace"]
    expected_result = "Invalid cards"

    # Act
    score = blackjack_score(hand)

    # Assert
    assert score == expected_result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():

    hand = [3, 4, 5, "Jack", "Ace"]
    expected_result = "bust"

    # Act
    score = blackjack_score(hand)

    # Assert
    assert score == expected_result


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():

    hand = ["Ace", "King", "Ace"]
    expected_result = 12

    # Act
    score = blackjack_score(hand)

    # Assert
    assert score == expected_result


# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():

    hand = ["Ace", "Ace", "Ace", "Ace"]
    expected_result = 14

    # Act
    score = blackjack_score(hand)

    # Assert
    assert score == expected_result
