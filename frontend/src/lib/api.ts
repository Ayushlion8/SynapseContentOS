const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api"

async function fetchAPI(endpoint: string, options?: RequestInit) {
  const res = await fetch(`${API_BASE}${endpoint}`, {
    headers: { "Content-Type": "application/json", ...options?.headers },
    ...options,
  })
  if (!res.ok) throw new Error(`API Error: ${res.status}`)
  return res.json()
}

export const api = {
  channels: {
    list: () => fetchAPI("/channels"),
    get: (id: string) => fetchAPI(`/channels/${id}`),
    health: (id: string) => fetchAPI(`/channels/${id}/health`),
    byNiche: (niche: string) => fetchAPI(`/channels/niche/${niche}`),
    dashboardStats: () => fetchAPI("/channels/stats/dashboard"),
  },
  trends: {
    list: () => fetchAPI("/trends"),
    emerging: () => fetchAPI("/trends/emerging"),
    viral: () => fetchAPI("/trends/viral"),
    byNiche: (niche: string) => fetchAPI(`/trends/niche/${niche}`),
    radar: () => fetchAPI("/trends/radar"),
    heatmap: () => fetchAPI("/trends/heatmap"),
  },
  agents: {
    list: () => fetchAPI("/agents"),
    run: (type: string, input: Record<string, unknown>) =>
      fetchAPI(`/agents/${type}/run`, { method: "POST", body: JSON.stringify(input) }),
    activity: () => fetchAPI("/agents/activity"),
  },
  pipeline: {
    generateReel: (data: { channel_id: string; niche?: string; custom_prompt?: string; trend_id?: string }) =>
      fetchAPI("/pipeline/generate-reel", { method: "POST", body: JSON.stringify(data) }),
    active: () => fetchAPI("/pipeline/active"),
    status: (id: string) => fetchAPI(`/pipeline/${id}/status`),
    feedbackLoop: (data: { channel_id: string; niche: string }) =>
      fetchAPI("/pipeline/feedback-loop", { method: "POST", body: JSON.stringify(data) }),
  },
  knowledge: {
    graph: () => fetchAPI("/knowledge/graph"),
    clusters: () => fetchAPI("/knowledge/clusters"),
    clusterDetail: (id: string) => fetchAPI(`/knowledge/clusters/${id}`),
  },
  analytics: {
    dashboard: () => fetchAPI("/analytics/dashboard"),
    feedbackLog: () => fetchAPI("/analytics/feedback-log"),
  },
}
