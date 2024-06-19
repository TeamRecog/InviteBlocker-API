def individual_serial(site) -> dict:
    return {
        "id": str(site["_id"]),
        "domain": site["domain"],
        "notes": site["notes"],
        "path": site["path"],
        "reason": site["reason"]
    }


def list_serial(sites) -> list:
    return (individual_serial(site) for site in sites)
