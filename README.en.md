# ROS and Arabic Voice Home Automation Learning Project

[العربية](README.md) | English

An educational project for Robot Operating Systems course 204. It connects ROS fundamentals, simulation, conversation, and embedded control. The first application is switching a lamp on and off using Arabic commands.

## Current status

The repository contains the initial structure and a text command demo with a simulated lamp. Speech recognition, ROS integration, physical control, and external services are planned features.

## Target environments

| Track | Hardware | Operating system | Validation |
| --- | --- | --- | --- |
| Learner | Raspberry Pi 4 | Ubuntu 20.04, 64 bit | Hardware validation pending |
| Development | Raspberry Pi 5 | A supported OS, to be confirmed | Hardware validation pending |

Ubuntu 20.04 is not an officially supported native installation on Pi 5. Each hardware path needs separate validation. See [environments](docs/environments.md).

## Run the first demo

On Linux, from the repository directory, with Python 3.8 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m arabic_home --command "شغل اللمبة"
python -m arabic_home --command "طفي اللمبة"
```

The first command displays “اللمبة الافتراضية: تعمل” (simulated lamp: on); the second displays “اللمبة الافتراضية: مطفأة” (simulated lamp: off). Each invocation is independent. No state is saved and no hardware is accessed.

## Repository layout

| Directory | Purpose |
| --- | --- |
| `docs/` | Architecture, environments, course mapping, and roadmap |
| `lessons/` | Guided experiments, expected results, and exercises |
| `src/arabic_home/` | Command interpretation and runnable text demo |
| `ros/` | Future ROS packages and launch files |
| `simulation/` | Future robot descriptions and simulation examples |
| `config/` | Environment configuration examples once selected |
| `hardware/` | Parts and wiring instructions once confirmed |
| `integrations/` | Optional AI model and WhatsApp integrations |
| `references/` | Course source index |
| `.github/` | Issue and contribution templates |

## Learning materials

Start with the [course map](docs/course-map.md), [roadmap](docs/roadmap.md), [architecture](docs/architecture.md), and [first lesson](lessons/01-text-lamp/README.md). These documents include Arabic and English sections. Read the [contribution guide](CONTRIBUTING.md) before proposing a change.

The original course PDF remains local because it contains contact information. No reuse license has been selected yet; the project owner will decide before public release.
