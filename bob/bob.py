def response(hey_bob:str) -> str:
    bob_responses_dict = {
        "for_question": "Sure.",
        "for_yelling": "Whoa, chill out!",
        "for_yell_a_question": "Calm down, I know what I'm doing!",
        "for_silence": "Fine. Be that way!",
        "for_anything_else": "Whatever."
    }

    hey_bob = hey_bob.rstrip()

    if hey_bob.endswith('?') and hey_bob.isupper():
        return bob_responses_dict["for_yell_a_question"]
    elif hey_bob.isupper():
        return bob_responses_dict["for_yelling"]
    elif hey_bob.endswith('?'):
        return bob_responses_dict["for_question"]
    elif len(hey_bob) == 0:
        return bob_responses_dict["for_silence"]
    else:
        return bob_responses_dict["for_anything_else"]