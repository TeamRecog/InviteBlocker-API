from fastapi import APIRouter
from models.site import IllegalSite
from config.database import sites_collection
from schema.schemas import siteEntities


router = APIRouter()

# GET /sites Returns all blacklisted sites


@router.get("/sites")
async def get_sites() -> list[IllegalSite]:
    sites = siteEntities(sites_collection.find())
    return sites


# GET /sites/$domain Returns specific blacklisted site
@router.get("/sites/{domain}")
async def get_site(domain) -> list[IllegalSite]:
    sites = siteEntities(sites_collection.find({"domain": domain}))
    return sites


# GET /stats Returns total count of blaclisted websites
@router.get("/stats")
async def get_stats():
    sites = siteEntities(sites_collection.find())
    return {
        "sites": len(list(sites))
    }
