"""
Endpoints for managing announcements in the High School Management System API
"""

from fastapi import APIRouter

from ..database import announcements_collection

router = APIRouter(
    prefix="/announcement",
    tags=["announcement"]
)


@router.get("")
def get_announcement():
    """Get the current active announcement"""
    announcement = announcements_collection.find_one({"_id": "current"})
    if announcement and announcement.get("active"):
        return {"message": announcement["message"], "active": True}
    return {"message": "", "active": False}
