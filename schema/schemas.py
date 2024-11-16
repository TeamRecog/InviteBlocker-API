def inviteEntity(invite) -> dict:
    return {
        "id": str(invite["_id"]),
        "invite": "https://discord.gg/" + invite["domain"],
        "notes": invite["notes"],
        "path": invite["path"],
        "reason": invite["reason"]
    }


def inviteEntities(invites) -> list:
    return [inviteEntity(invite) for invite in invites]
