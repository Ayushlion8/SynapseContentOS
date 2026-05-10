from fastapi import APIRouter
from app.services.knowledge_graph import knowledge_graph

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


@router.get("/graph")
async def get_knowledge_graph():
    return knowledge_graph.get_graph()


@router.get("/clusters")
async def get_clusters():
    graph = knowledge_graph.get_graph()
    return {"clusters": graph["clusters"], "stats": graph["stats"]}


@router.get("/clusters/{cluster_id}")
async def get_cluster_detail(cluster_id: str):
    return knowledge_graph.get_cluster_detail(cluster_id)
