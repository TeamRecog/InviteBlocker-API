from pydantic import BaseModel


class IllegalInvite(BaseModel):
    invite: str
    notes: str
    path: str
    reason: str
