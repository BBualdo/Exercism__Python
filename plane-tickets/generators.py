"""Functions to automate Conda airlines ticketing system."""
import math


def generate_seat_letters(number:int) -> iter:
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = "ABCD"
    for num in range(number):
        yield seats[num % 4]


def generate_seats(number:int) -> iter:
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats = "ABCD"
    for num in range(1, number + 1):
        row = math.ceil(num / 4)
        if row >= 13: row += 1
        yield f"{row}{seats[(num - 1) % 4]}"

def assign_seats(passengers:list[str]) -> dict:
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    result = {}
    seats = generate_seats(len(passengers))
    for passenger in passengers:
        result[passenger] = next(seats)

    return result

def generate_codes(seat_numbers:list[str], flight_id:str) -> iter:
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        yield f"{seat_number}{flight_id}".ljust(12, "0")
