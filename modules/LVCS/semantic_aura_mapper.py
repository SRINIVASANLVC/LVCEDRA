"""
semantic_aura_mapper.py

Generates aura overlays for civic zones based on SPL routing and archetypal stress.
Used to visualize karmic diffusion and polarity saturation across the urban lattice.
"""

import matplotlib.pyplot as plt

def generate_aura_map(routing_plan, archetype_map, polarity_index):
    """
    Creates a symbolic aura map showing stress intensity per zone.
    """
    zone_intensity = {}
    for spl_id, zone_id in routing_plan.items():
        archetype = archetype_map.get(spl_id.split('-')[-1], "Unknown")
        base_intensity = {
            "Assertion": 0.8,
            "Constraint": 0.9,
            "Imprinting": 0.7,
            "Attachment": 0.6,
            "Detachment": 0.5,
            "Translation": 0.65,
            "Expansion": 0.75,
            "Obsession": 0.85,
            "Identity": 0.8
        }.get(archetype, 0.6)
        adjusted = round(base_intensity * (1 + polarity_index), 2)
        zone_intensity[zone_id] = zone_intensity.get(zone_id, 0) + adjusted

    # Visualization (symbolic, not geographic)
    zones = list(zone_intensity.keys())
    intensities = list(zone_intensity.values())
    colors = ['#f94144', '#f3722c', '#f8961e', '#f9c74f', '#90be6d', '#43aa8b', '#577590']

    plt.figure(figsize=(10, 6))
    plt.bar(zones, intensities, color=colors[:len(zones)])
    plt.title("Semantic Aura Map — Zone Stress Intensity")
    plt.xlabel("Modulation Zones")
    plt.ylabel("Stress Intensity")
    plt.tight_layout()
    plt.show()
