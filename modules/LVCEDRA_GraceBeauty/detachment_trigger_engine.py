"""
detachment_trigger_engine.py

Monitors emotional tolerance and detachment thresholds from family templates.
Triggers symbolic detachment when SPL stress exceeds encoded limits.
"""

from modules.LVCS.release_protocols import release_stress
import json

def load_template_db(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)["templates"]

def check_detachment_eligibility(spl_id, buffer_weight, template_db):
    """
    Returns True if buffer_weight exceeds template tolerance threshold.
    """
    for template in template_db:
        if spl_id in template.get("preferred_zones", []):  # Simplified mapping
            threshold = template.get("detachment_threshold", 1.0)
            return buffer_weight > threshold
    return False

def trigger_detachment(spl_id, buffer_weight, template_db, ritual_protocol="Water Release"):
    """
    If eligible, applies symbolic release and marks detachment event.
    """
    if check_detachment_eligibility(spl_id, buffer_weight, template_db):
        released_weight = release_stress(ritual_protocol, buffer_weight)
        return {
            "SPL_ID": spl_id,
            "Status": "Detached",
            "ReleasedWeight": released_weight,
            "Protocol": ritual_protocol
        }
    else:
        return {
            "SPL_ID": spl_id,
            "Status": "Retained",
            "BufferWeight": buffer_weight
        }
