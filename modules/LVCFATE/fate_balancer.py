# - Polarity index reflects emotional tone across planetary signs
# - Buffering logic prevents SPL overload during high karmic stress
# - This module complements LVCS routing by softening compression edges
# - Future expansion: integrate emotional archetypes and civic overlays
"""
fate_balancer.py

Balances polarity stress across SPL overlays using planetary modulation and emotional tone.
Used to prevent overload in jiva templates and redirect karmic tension through semantic buffers.
"""

def calculate_polarity_index(planet_positions):
    """
    Calculates polarity index based on planetary distribution.
Returns a float between -1.0 (extreme negative) and +1.0 (extreme positive).
"""
    polarity_score = 0
    for planet, (sign, degree) in planet_positions.items():
        if sign in ['Aries', 'Leo', 'Sagittarius']:
            polarity_score += 0.1
        elif sign in ['Cancer', 'Scorpio', 'Pisces']:
            polarity_score -= 0.1
        # Add more nuanced mappings as needed
    return round(polarity_score, 3)

def apply_compression_buffer(polarity_index, spl_overlay):
    """
    Applies semantic buffering based on polarity index and SPL stress zones.
Returns a dictionary of SPL zones with adjusted stress weights.
"""
    buffered_SPLs = {}
    for spl_id, planets in spl_overlay.items():
        base_weight = len(planets)
        adjustment = polarity_index * 0.5  # scale factor
        buffered_SPLs[spl_id] = round(base_weight + adjustment, 2)
    return buffered_SPLs

def generate_fate_balance_chart(planet_positions, spl_overlay):
    """
    Full pipeline: calculates polarity, applies buffer, returns fate chart.
"""
    polarity_index = calculate_polarity_index(planet_positions)
    buffered_SPLs = apply_compression_buffer(polarity_index, spl_overlay)
    return {
        'PolarityIndex': polarity_index,
        'BufferedSPLs': buffered_SPLs
    }
