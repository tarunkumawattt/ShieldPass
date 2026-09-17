"""
ShieldPass - Password Strength Assessment & Generation Engine
Python Implementation (1:1 translation of JavaScript logic)
"""

import math
import re
import random
import string

STRENGTH_LEVELS = {
    0: {"label": "Very Weak", "color": "Red"},
    1: {"label": "Weak", "color": "Orange"},
    2: {"label": "Medium", "color": "Yellow"},
    3: {"label": "Strong", "color": "Green"},
    4: {"label": "Very Strong", "color": "Cyan"},
}


def get_password_strength(password):
    """
    Evaluates password strength based on length, character complexity,
    common sequential patterns, and Shannon entropy.
    """
    if not password:
        return {
            "score": 0.0,
            "label": "Very Weak",
            "entropy": 0,
            "complexity_count": "0 / 4",
            "crack_time": "Seconds",
            "feedback": ["Enter a password to begin analysis."],
        }

    feedback = []
    score = 0.0

    # 1. Length Check
    if len(password) >= 8:
        score += 1.0
    else:
        feedback.append("Make it at least 8 characters long.")

    if len(password) >= 12:
        score += 0.5

    # 2. Character Complexity Checks
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_number = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    complexity_count = sum([has_lower, has_upper, has_number, has_special])

    if has_lower and has_upper:
        score += 1.0
    else:
        feedback.append("Mix uppercase and lowercase letters.")

    if has_number:
        score += 1.0
    else:
        feedback.append("Add at least one number.")

    if has_special:
        score += 1.0
    else:
        feedback.append("Use special characters (e.g., !, @, #).")

    # 3. Penalty for common patterns & sequential characters
    pattern_match = re.search(r"(123|abc|qwerty|password)", password, re.IGNORECASE)
    if pattern_match:
        score = max(0.0, score - 1.5)
        feedback.append('Avoid common patterns like "123" or "password".')

    # 4. Entropy Calculation: length * log2(charset_size)
    charset_size = 0
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_number:
        charset_size += 10
    if has_special:
        charset_size += 32

    entropy = int(round(len(password) * (math.log(charset_size or 1) / math.log(2))))

    # Clamp score to 0..4
    final_score = min(4.0, max(0.0, score))
    rounded_index = int(math.floor(final_score))
    strength_info = STRENGTH_LEVELS.get(rounded_index, STRENGTH_LEVELS[0])

    # Estimated crack time heuristic
    if entropy > 60:
        crack_time = "Centuries"
    elif entropy > 40:
        crack_time = "Years"
    else:
        crack_time = "Seconds"

    return {
        "score": final_score,
        "label": strength_info["label"],
        "entropy": entropy,
        "complexity_count": str(complexity_count) + " / 4",
        "crack_time": crack_time,
        "feedback": feedback if feedback else ["Your password meets all basic security criteria!"],
    }


def generate_password(length=16):
    """
    Generates a cryptographically strong random password using random.SystemRandom.
    """
    charset = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + "!@#$%^&*()_+~`|}{[]:;?><,./-="
    )
    secure_random = random.SystemRandom()
    return "".join(secure_random.choice(charset) for _ in range(length))


if __name__ == "__main__":
    print("=" * 55)
    print(" ShieldPass - Python Password Evaluator ")
    print("=" * 55)

    # Demo 1: Random generated strong password
    strong_pwd = generate_password(16)
    print("\nGenerated Strong Password: " + strong_pwd)
    analysis = get_password_strength(strong_pwd)
    print("Strength   : {0} ({1}/4)".format(analysis['label'], analysis['score']))
    print("Entropy    : {0} bits".format(analysis['entropy']))
    print("Crack Time : {0}".format(analysis['crack_time']))
    print("Feedback   : {0}".format(", ".join(analysis['feedback'])))

    # Demo 2: Interactive password input
    print("\n" + "-" * 55)
    try:
        get_input = raw_input
    except NameError:
        get_input = input

    user_input = get_input("Enter a password to test (or press Enter to skip): ").strip()
    if user_input:
        user_analysis = get_password_strength(user_input)
        print("\nAnalysis Result:")
        print(" - Strength: {0} (Score: {1}/4)".format(user_analysis['label'], user_analysis['score']))
        print(" - Entropy: {0} bits".format(user_analysis['entropy']))
        print(" - Charset Complexity: {0}".format(user_analysis['complexity_count']))
        print(" - Est. Crack Time: {0}".format(user_analysis['crack_time']))
        print(" - Suggestions:")
        for tip in user_analysis["feedback"]:
            print("    * " + tip)

#AUTHOR : TARUN KUMAR
