from typing import Dict, Any, List
import uuid
import random


class KnowledgeGraphService:
    """Content Knowledge Graph — visualizes content relationships, viral clusters, hook families, audience segments."""

    def __init__(self):
        self._nodes = self._generate_nodes()
        self._edges = self._generate_edges()
        self._clusters = self._generate_clusters()

    def _generate_nodes(self) -> List[Dict[str, Any]]:
        node_types = [
            ("hook", ["contrarian_hook", "question_hook", "shocking_stat_hook", "curiosity_gap_hook", "challenge_hook", "relatable_hook", "storytelling_hook", "fear_hook"]),
            ("format", ["step_by_step", "countdown_list", "before_after", "pov_format", "silent_demo", "talking_head", "screen_recording", "asmr_style"]),
            ("emotion", ["curiosity", "fear", "aspiration", "surprise", "urgency", "social_proof", "nostalgia", "controversy"]),
            ("audience", ["gen_z_male", "millennial_female", "gen_z_female", "millennial_male", "gen_x_professional"]),
            ("trend", ["ai_tools", "fitness_transformation", "budget_hacks", "stoic_philosophy", "food_asmr", "passive_income"]),
            ("niche", ["fitness", "tech", "motivation", "food", "finance"]),
            ("content", ["reel_001", "reel_002", "reel_003", "reel_004", "reel_005", "reel_006", "reel_007", "reel_008"]),
        ]

        nodes = []
        for ntype, labels in node_types:
            for label in labels:
                nodes.append({
                    "id": f"{ntype}_{label}",
                    "type": ntype,
                    "label": label.replace("_", " ").title(),
                    "weight": round(random.uniform(0.3, 1.0), 2),
                    "performance_score": round(random.uniform(0.4, 0.95), 2),
                    "cluster": random.choice(["alpha", "beta", "gamma", "delta", "epsilon"]),
                    "x": random.uniform(-500, 500),
                    "y": random.uniform(-500, 500),
                    "z": random.uniform(-100, 100),
                })
        return nodes

    def _generate_edges(self) -> List[Dict[str, Any]]:
        edge_patterns = [
            ("hook", "format", "used_in"),
            ("hook", "emotion", "triggers"),
            ("format", "trend", "adapts"),
            ("emotion", "audience", "resonates_with"),
            ("audience", "niche", "belongs_to"),
            ("trend", "niche", "relevant_to"),
            ("content", "hook", "uses"),
            ("content", "format", "follows"),
            ("content", "emotion", "evokes"),
            ("content", "trend", "leveraged"),
            ("hook", "hook", "variation_of"),
            ("format", "format", "evolved_from"),
        ]

        edges = []
        for source_type, target_type, relation in edge_patterns:
            source_nodes = [n for n in self._nodes if n["type"] == source_type]
            target_nodes = [n for n in self._nodes if n["type"] == target_type]

            count = min(len(source_nodes), len(target_nodes), random.randint(3, 8))
            for _ in range(count):
                s = random.choice(source_nodes)
                t = random.choice(target_nodes)
                if s["id"] != t["id"]:
                    edges.append({
                        "source": s["id"],
                        "target": t["id"],
                        "relationship": relation,
                        "weight": round(random.uniform(0.3, 1.0), 2),
                        "strength": random.choice(["strong", "medium", "weak"]),
                    })
        return edges

    def _generate_clusters(self) -> List[Dict[str, Any]]:
        return [
            {"id": "alpha", "name": "Viral Hook Cluster", "node_count": 12, "avg_performance": 0.82, "dominant_type": "hook"},
            {"id": "beta", "name": "Educational Format Cluster", "node_count": 8, "avg_performance": 0.71, "dominant_type": "format"},
            {"id": "gamma", "name": "Emotional Trigger Cluster", "node_count": 10, "avg_performance": 0.78, "dominant_type": "emotion"},
            {"id": "delta", "name": "Audience Segment Cluster", "node_count": 6, "avg_performance": 0.65, "dominant_type": "audience"},
            {"id": "epsilon", "name": "Cross-Niche Trend Cluster", "node_count": 9, "avg_performance": 0.74, "dominant_type": "trend"},
        ]

    def get_graph(self) -> Dict[str, Any]:
        return {
            "nodes": self._nodes,
            "edges": self._edges,
            "clusters": self._clusters,
            "stats": {
                "total_nodes": len(self._nodes),
                "total_edges": len(self._edges),
                "total_clusters": len(self._clusters),
                "avg_node_weight": round(sum(n["weight"] for n in self._nodes) / len(self._nodes), 2),
                "top_cluster": max(self._clusters, key=lambda c: c["avg_performance"])["name"],
            },
        }

    def get_cluster_detail(self, cluster_id: str) -> Dict[str, Any]:
        cluster = next((c for c in self._clusters if c["id"] == cluster_id), None)
        if not cluster:
            return {"error": "Cluster not found"}
        nodes = [n for n in self._nodes if n["cluster"] == cluster_id]
        node_ids = [n["id"] for n in nodes]
        edges = [e for e in self._edges if e["source"] in node_ids or e["target"] in node_ids]
        return {
            **cluster,
            "nodes": nodes,
            "edges": edges,
        }


knowledge_graph = KnowledgeGraphService()
