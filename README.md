# Madinah Heat Analysis: Cooling Priority & Pedestrian Movement (Tasks 5 & 6)

This repo holds two interactive web maps built from open data (OpenStreetMap / Geofabrik) and a walking network model.

**Open:** download `web/Madinah_Cooling_Pedestrian_Maps.html` and open it in Chrome. The basemap needs an internet connection.

## Map 01: Priority Areas for Cooling (Task 5)
- Cooling Priority Index on hexagons: 40% sensitive uses + 35% pedestrian movement + 25% shade deficit.
- Sensitive uses include mosques, schools, bus stations, malls, parks, walkways and road junctions.
- Each building has a 20 m cooling perimeter.
- Umbrella suitability model on 8 m cells: 30% heat, 30% footfall, 20% sun exposure, 20% sidewalk access.
- Cells on buildings, roads or under existing tree shade are excluded.
- Action-Requirement Plan:
  - ☂ 10,943 umbrellas (100 m², short-term)
  - 🌳 2,382 site trees
  - 🌳 195,935 street trees (200 m² canopy, long-term programme)

## Map 02: Pedestrian Movement (Task 6)
- Pedestrian Movement Index with hotspots and animated corridors.
- 700 simulated pedestrians walk shortest paths to Masjid an-Nabawi.
- 5/10/15-min walking catchments, with minute labels on the network.
- A→B tool:
  - Compares the fastest route with a cool route.
  - Shows ☂ shade stops and the longest walk in the sun.
  - Builds a route shade plan: a new umbrella wherever there is ≥100 m without shade, and trees every 10 m on both kerbs.
  - Lists mosques, malls, parks and bus stops along the way.
- Validated against PedestrianCatch: median difference 0.79 min, 93.8% within ±2 min.

## Files
| File | Purpose |
|---|---|
| `web/Madinah_Cooling_Pedestrian_Maps.html` | Final deliverable (data embedded) |
| `web/template.html` | Map UI (MapLibre GL) |
| `web/build_web_data.py` | ArcGIS Pro (arcpy) pipeline: CPI, suitability, umbrellas/trees, network model |
| `web/inject.py` | Puts the data into the template, for UI-only changes |
| `Action_Requirement_Plan.csv` | Site-by-site umbrellas / trees |

The analysis layers live in `Madinah_Analysis.gdb`, which is not in the repo because of its size.
