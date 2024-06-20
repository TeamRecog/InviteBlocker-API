def siteEntity(site) -> dict:
    return {
        "id": str(site["_id"]),
        "domain": site["domain"],
        "notes": site["notes"],
        "path": site["path"],
        "reason": site["reason"]
    }


def siteEntities(sites) -> list:
    return (siteEntity(site) for site in sites)
