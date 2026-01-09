from agents.medical_agent import MedicalAgent
from agents.explain_agent import ExplainAgent
from agents.translate_agent import TranslateAgent
from agents.voice_agent import VoiceAgent

# Initialize agents
medical_agent = MedicalAgent()
explain_agent = ExplainAgent()
translate_agent = TranslateAgent()
voice_agent = VoiceAgent()

# Sample medical report
report_text = """
Patient has Hemoglobin level of 9 g/dL.
Normal range is 13-17 g/dL.
"""

# 🌍 Language selection (HINGLISH is DEFAULT)
print("\n🌍 Select output language (press Enter for Hinglish default):")
print("hi  / hindi     → Hindi")
print("mr  / marathi   → Marathi")
print("ta  / tamil     → Tamil")
print("bho / bhojpuri  → Bhojpuri")
print("hinglish        → Hinglish (default)")

user_input = input("Enter language (optional): ").strip().lower()

LANGUAGE_MAP = {
    "": "hinglish",          # ENTER → Hinglish
    "hinglish": "hinglish",

    "hi": "hi",
    "hindi": "hi",

    "mr": "mr",
    "marathi": "mr",

    "ta": "ta",
    "tamil": "ta",

    "bho": "bho",
    "bhojpuri": "bho"
}

target_lang = LANGUAGE_MAP.get(user_input, "hinglish")

print("\n🔍 Analyzing report...")
analysis = medical_agent.analyze_report(report_text)
print(analysis)

# 🔥 DEFAULT: HINGLISH
if target_lang == "hinglish":
    print("\n🧾 Explaining in Hinglish (default)...")
    final_text = explain_agent.simplify(analysis, style="hinglish")
    voice_lang = "hi"   # Hindi voice for Hinglish

else:
    print("\n🧾 Explaining in simple English...")
    simple_text = explain_agent.simplify(analysis)

    print(f"\n🌍 Translating to {target_lang}...")
    final_text = translate_agent.translate(simple_text, target_lang)
    voice_lang = target_lang

print(final_text)

print("\n🔊 Generating voice...")
audio_file = voice_agent.generate_voice(final_text, voice_lang)

if audio_file:
    print("Audio saved at:", audio_file)
else:
    print("🔇 Audio not generated (network issue). Text output is available.")
