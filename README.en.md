<div dir="ltr" lang="en">

# Robot Operating Systems

**Course code in the outline: 204 روبوت** · [العربية](README.md)

The repository organizes the course into six units, each with separate directories for syllabus items and exercises. Every lab documents Arabic and English explanations, prerequisites, hardware, setup, and actual results. Extensions have their own catalog.

## Educational content

[Weekly course presentations](PPT/README.md) are available as PDF files for weeks 1–16. Use them for teaching and review alongside the practical lab guides.

## Start here

1. Read the [syllabus map](course/syllabus-map.md) and [detailed item index](course/exercises-index.md).
2. Choose a [unit](labs/README.md), then the exercise by its syllabus reference.
3. Select an [environment](environments/README.md), and check [hardware and wiring](hardware/README.md).
4. Follow the lab and record [validation](validation/README.md).

Embedded systems has four separate integration exercises: Arduino, STM32, Raspberry Pi and Odroid. Weekly assessment counts are not detailed exercise counts.

## Layout

| Directory | Contents |
| --- | --- |
| course | Syllabus map and detailed item index |
| PPT | Weekly course presentations in PDF format, weeks 1–16 |
| labs | ROS fundamentals, setup, mobile simulation, arm simulation, conversation and speech, embedded systems |
| extensions | Language models, WhatsApp, and integrated voice home automation |
| environments | Board and OS profiles |
| hardware | Parts inventory and wiring requirements |
| validation | Actual runs and compatibility matrix |
| docs | Architecture, roadmap, lab template, writing rules |
| references | Source index |

Keep each exercise's documentation, source, configuration, and ROS or simulation assets within its directory. Keep extension applications separate from original course coverage.

## Available implementation

The [text lamp demo](labs/06-embedded-systems/03-raspberry-pi/01-text-lamp/README.md) is preparation within the Raspberry Pi lab. It does not implement physical control or ROS integration. Other guides define planned scope rather than completed applications.

From the repository root on Linux with Python 3.8 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m arabic_home --command "شغل اللمبة"
python -m arabic_home --command "طفي اللمبة"
```

The phrases mean turn on and turn off the lamp. Output reports the simulated state. Each invocation is independent; no state is persisted and no device is accessed.

## Board paths

Pi 4 targets arm64 Ubuntu 20.04 for course alignment. Pi 5 has a proposed arm64 Ubuntu 24.04 path. Neither has hardware validation yet. For other embedded labs, record a Pi execution host separately from its connected board. OS support alone does not establish audio, GPIO or ROS support; see the [environment decisions](docs/environments.md).

Read the [architecture](docs/architecture.md), [roadmap](docs/roadmap.md), [contribution guide](CONTRIBUTING.md), [lab template](docs/lesson-template.md) and [text direction guide](docs/writing-style.md). The repository is public and its educational content is accessible to everyone. Reuse licensing remains a course owner decision. The original outline stays local due to contact details.

</div>
