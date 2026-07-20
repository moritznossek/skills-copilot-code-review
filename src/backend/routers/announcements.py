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
    """Get the current active announcement.

    Returns a dict with 'message' (str) and 'active' (bool).
    When no active announcement exists, 'message' is empty and 'active' is False.
    """
    announcement = announcements_collection.find_one({"_id": "current"})
    if announcement and announcement.get("active"):
        return {"message": announcement.get("message", ""), "active": True}
    return {"message": "", "active": False}
