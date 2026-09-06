# KERYON FLIGHT LAB

A browser-based 3D UAV research and flight-test simulator for autonomy, navigation, resilience and mission-planning experiments.

## Current prototype

- 3D procedural test range
- Generic MALE-class, heavy UAV-class and VTOL-class research profiles
- Simplified flight dynamics
- Airspeed, altitude, heading, endurance and energy telemetry
- Wind disturbance
- GPS degradation scenario
- Data-link degradation
- Propulsion degradation
- Mountain survey / terrain scenario
- Autonomous heading and altitude hold
- Event log and live vehicle-health panel
- Desktop and mobile browser support

The aircraft classes are generic research profiles. References such as “TB2-scale” or “Akıncı-scale” describe only a broad size/use class and are **not exact simulations of proprietary aircraft performance**.

## Safety scope

KERYON Flight Lab is intentionally focused on non-weaponized flight research. Weapon employment, targeting, strike planning and offensive mission logic are not modeled.

## Run locally

Because the demo uses ES modules, serve it through any static HTTP server instead of opening `index.html` directly.

```bash
python -m http.server 8080
```

Then open `http://localhost:8080/KERYON_FLIGHT_LAB/`.

## Architecture

- `index.html` — application shell and telemetry UI
- `styles.css` — KERYON visual system and responsive layout
- `app.js` — Three.js world, UAV model, scenario engine and flight simulation
- `vercel.json` — static hosting configuration

## Roadmap

Planned safe research features include richer aerodynamics, configurable environmental models, replay/telemetry export, multi-UAV deconfliction, path-planning benchmarks, sensor visualization, digital-twin model import, hardware-in-the-loop interfaces and reproducible experiment files.

---

**KERYON DYNAMICS — Intelligence in Motion**
