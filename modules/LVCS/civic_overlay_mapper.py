"""
civic_overlay_mapper.py

Maps semantic modulation zones to real-world urban coordinates and civic overlays.
Used by LVCS routing engine to localize stress mapping within actual geography.
"""

ZONE_COORDINATES = {
    "Z01": {"district": "Oak Cliff", "lat": 32.7157, "lon": -96.8250},
    "Z12": {"district": "Fair Park", "lat": 32.7761, "lon": -96.7600},
    "Z22": {"district": "Uptown", "lat": 32.8007, "lon": -96.8050},
    "Z09": {"district": "Pleasant Grove", "lat": 32.7160, "lon": -96.6510}
}

STRESS_VECTORS = {
    "Constraint": ["Transit Congestion", "Zoning Rigidity", "Industrial Saturation"],
    "Imprinting": ["School Pipeline", "Police Overpresence", "Surveillance Density"],
    "Attachment": ["Real Estate Volatility", "Family Displacement", "Identity Clustering"]
}

def map_zone_to_coordinates(zone_id):
    """
    Returns district and coordinates for given zone_id.
    """
    return ZONE_COORDINATES.get(zone_id, {"district": "Unknown", "lat": 0.0, "lon": 0.0})

def map_archetype_to_stress(archetype):
    """
    Returns real-world civic stress types linked to emotional archetype.
    """
    return STRESS_VECTORS.get(archetype, ["Generic Urban Fatigue"])

def generate_civic_overlay(routing_map, archetype_map):
    """
    Produces overlay connecting routed SPL zones to geography and civic tension themes.
    """
    overlay = {}
    for spl_id, zone_id in routing_map.items():
        coords = map_zone_to_coordinates(zone_id)
        archetype = archetype_map.get(spl_id.split('-')[-1], "Unknown")
        stress_types = map_archetype_to_stress(archetype)
        overlay[spl_id] = {
            "ZoneID": zone_id,
            "District": coords["district"],
            "Coordinates": (coords["lat"], coords["lon"]),
            "Archetype": archetype,
            "StressVectors": stress_types
        }
    return overlay
