from backend.gemini_debater import generate_argument

from .gemini_debater import generate_argument

def debate_rounds(topic, user_stance, bot_stance, n_rounds):
    transcript = []
    for round_num in range(n_rounds):
        # Generate user argument
        user_argument = generate_argument(topic, user_stance)
        transcript.append(("User", user_argument))

        # Generate bot argument
        bot_argument = generate_argument(topic, bot_stance)
        transcript.append(("Bot", bot_argument))

    return transcript
