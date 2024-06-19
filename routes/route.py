from fastapi import APIRouter
from models.sites import IllegalSite
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId


router = APIRouter()

# GET /sites Returns all blacklisted sites


@router.get("/sites")
async def get_sites() -> list[IllegalSite]:
    sites = list_serial(collection_name.find())
    return sites


# GET /sites/$domain Returns specific blacklisted site
@router.get("/sites/{domain}")
async def get_site(domain) -> list[IllegalSite]:
    sites = list_serial(collection_name.find({"domain": domain}))
    return sites


# GET /stats Returns total count of blaclisted websites
@router.get("/stats")
async def get_stats():
    sites = list_serial(collection_name.find())
    return {
        "sites": len(list(sites))
    }


# # POST /sites Adds new site to our list
# @router.post("/sites")
# def post_site(site: IllegalSite):
#     collection_name.insert_one(dict(site))


# # PUT /sites/ID Overwrites site with ID with new data
# @router.put("/sites/{id}")
# def put_site(id: str, site: IllegalSite):
#     collection_name.find_one_and_update(
#         {"_id": ObjectId(id)}, {"$set": dict(site)})
