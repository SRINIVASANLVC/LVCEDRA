from LVCS.modulation import apply_SPL_overlay

def generate_matrix(archetype_id, spl_id):
    matrix = apply_SPL_overlay(archetype_id, spl_id)
    return matrix