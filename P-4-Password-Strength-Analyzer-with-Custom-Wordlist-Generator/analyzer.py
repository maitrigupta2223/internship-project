from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)

    score = result['score']
    guesses = result['guesses']
    crack_time = result['crack_times_display']['offline_fast_hashing_1e10_per_second']

    return {
        "score": score,
        "guesses": guesses,
        "crack_time": crack_time
    }
