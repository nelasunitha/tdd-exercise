VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


def blackjack_score(hand):
    # Edge case: for hand with less than 2 elements and greater than 5 elements
    if len(hand) < 2 or len(hand) > 5:
        return "Invalid cards"

    score = 0
    face_cards = ["Jack", "Queen", "King"]
    aces_count = 0

    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid cards"

        # scoring 10 points for face cards
        if card in face_cards:
            score += 10

        # if the card is 'Ace' scoring 11 points and simultaneously checking for the ace count
        elif card == "Ace":
            aces_count += 1
            score += 11
        else:
            score += card
    # at end if score is > 21 and aces are present considering score point as 1 instead of 11
    while score > 21 and aces_count > 0:
        score -= 10
        aces_count -= 1

    return score if score <= 21 else "bust"
