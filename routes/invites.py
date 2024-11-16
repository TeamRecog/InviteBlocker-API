from fastapi import APIRouter
from models.invite import IllegalInvite
from config.database import invites_collection
from schema.schemas import inviteEntities


router = APIRouter()

# GET /invites
# Returns all blacklisted invites
@router.get("/invites")
async def get_invites() -> list[IllegalInvite]:
    invites = inviteEntities(invites_collection.find())
    return invites


# GET /invite/$invite_code
# Returns specific blacklisted invite
@router.get("/invite/{invite_code}")
async def get_invite(invite_code) -> list[IllegalInvite]:
    invites = inviteEntities(invites_collection.find({"invite": invite_code}))
    return invites


# GET /stats
# Returns total count of blacklisted invites
@router.get("/stats")
async def get_stats():
    invites = inviteEntities(invites_collection.find())
    return {
        "invites": len(list(invites))
    }
