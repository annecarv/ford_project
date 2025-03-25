from fastapi import APIRouter
from .vehicles import router as vehicles_router
""" from .parts import router as parts_router
from .suppliers import router as suppliers_router
from .locations import router as locations_router
from .purchases import router as purchases_router
from .warranties import router as warranties_router """

router = APIRouter()

# módulos das rotas
router.include_router(vehicles_router, prefix="/vehicles", tags=["Vehicles"])
""" router.include_router(parts_router, prefix="/parts", tags=["Parts"])
router.include_router(suppliers_router, prefix="/suppliers", tags=["Suppliers"])
router.include_router(locations_router, prefix="/locations", tags=["Locations"])
router.include_router(purchases_router, prefix="/purchases", tags=["Purchases"])
router.include_router(warranties_router, prefix="/warranties", tags=["Warranties"])
 """