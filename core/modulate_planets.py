"""
modulate_planets.py

Parses planetary positions from Lahiri Sidereal Ephemeris and maps them to SPL zones.
Used for systemic modulation, karmic routing, and overlay compression.
"""

import re
from datetime import datetime

def parse_ephemeris_text(ephemeris_text):
    """
    Parses raw ephemeris text and extracts planetary positions.
    Returns a dictionary: { 'Sun': (sign, degree), 'Moon': ..., ... }
    """
    planet_positions = {}
    lines = ephemeris_text.split('\n')
    for line in lines:
        match = re.match(r'(\w+)\s+(\w+)\s+(\d+\.\d+)', line)
        if match:
            planet, sign, degree = match.groups()
            planet_positions[planet] = (sign, float(degree))
    return planet_positions

def map_to_SPL(planet_positions, spl_config):
    """
    Maps planetary positions to SPL zones using predefined config.
    Returns a dictionary: { 'SPL047': ['Moon', 'Mars'], ... }
    """
    spl_map = {}
    for planet, (sign, degree) in planet_positions.items():
        for spl_id, spl_rule in spl_config.items():
            if spl_rule(sign, degree):
                spl_map.setdefault(spl_id, []).append(planet)
    return spl_map

def generate_modulation_chart(dob, ephemeris_text, spl_config):
    """
    Full pipeline: parses ephemeris, maps to SPL, returns modulation chart.
    """
    planet_positions = parse_ephemeris_text(ephemeris_text)
    spl_overlay = map_to_SPL(planet_positions, spl_config)
    return {
        'DOB': dob,
        'PlanetaryPositions': planet_positions,
        'SPLOverlay': spl_overlay
    }
