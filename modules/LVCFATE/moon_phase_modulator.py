"""
moon_phase_modulator.py

Modulates SPL buffering and detachment logic based on lunar phase.
Used to synchronize karmic routing with emotional tides and planetary echoes.
"""

from datetime import datetime
import math

def get_moon_phase(date=None):
    """
    Returns moon phase name based on date.
    """
    if date is None:
        date = datetime.utcnow()
    diff = date - datetime(2001, 1, 1)
    days = diff.days + (diff.seconds / 86400)
    lunations = days / 29.53058867
    phase_index = lunations % 1

    if phase_index < 0.03 or phase_index > 0.97:
        return "New Moon"
    elif phase_index < 0.22:
        return "Waxing Crescent"
    elif phase_index < 0.28:
        return "First Quarter"
    elif phase_index < 0.47:
        return "Waxing Gibbous"
    elif phase_index < 0.53:
        return "Full Moon"
    elif phase_index < 0.72:
        return "Waning Gibbous"
    elif phase_index < 0.78:
        return "Last Quarter"
    else:
        return "Waning Crescent"

def adjust_buffering_by_moon_phase(buffer_weight, phase):
    """
    Modifies SPL buffer weight based on lunar phase.
    """
    modifiers = {
        "New Moon": 0.85,
        "Waxing Crescent": 0.9,
        "First Quarter": 1.0,
        "Waxing Gibbous": 1.1,
        "Full Moon": 1.25,
        "Waning Gibbous": 1.1,
        "Last Quarter": 1.0,
        "Waning Crescent": 0.9
    }
    factor = modifiers.get(phase, 1.0)
    return round(buffer_weight * factor, 2)
