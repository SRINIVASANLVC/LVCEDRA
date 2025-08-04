from LVCS.modulation import get_zone_mapping

def route_archetype(archetype_id):
    zone = get_zone_mapping(archetype_id)
    return {"archetype_id": archetype_id, "modulation_zone": zone}