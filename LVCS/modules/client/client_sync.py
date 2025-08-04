from LVCS.ledger import fetch_nodal_truths

def sync_client_state(client_id):
    truths = fetch_nodal_truths(client_id)
    return {"client_id": client_id, "nodal_truths": truths}