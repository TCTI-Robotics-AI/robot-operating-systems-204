<div dir="ltr" lang="en">

# Robot Operating Systems

**Course code as shown in the outline: 204 روبوت** · [العربية](README.md)

This course repository contains independent labs for Linux, ROS, simulation, speech, conversation, and embedded control. Each lab has Arabic and English explanations, prerequisites, setup, hardware requirements, and validation records. Voice home automation and WhatsApp are individual applications within the wider course and its extensions.

## Start here

1. Read the [course map](docs/course-map.md) and [lab catalog](labs/README.md).
2. Choose your board in the [environment guide](environments/README.md).
3. Check the [hardware and wiring requirements](hardware/README.md).
4. Follow the lab and record results using the [validation guide](validation/README.md).

The available implementation is [text control of a simulated lamp](labs/07-gpio-control/01-text-lamp/README.md). Other directories describe planned scope rather than completed applications.

## Hardware support

Both Pi 4 and Pi 5 are target boards for instructors and learners. Document board specific OS, audio, and GPIO setup while retaining the same learning objective.

| Board | OS track | Project hardware validation |
| --- | --- | --- |
| Raspberry Pi 4 | 64 bit Ubuntu 20.04 for course alignment | Pending |
| Raspberry Pi 5 | 64 bit Ubuntu 24.04 as a proposed supported board OS | Pending |

Ubuntu 20.04 is not an officially supported native Pi 5 path. OS support does not establish compatibility of ROS, microphones, or GPIO libraries. Validate each lab separately; see [environment decisions and sources](docs/environments.md).

## Repository layout

The numbered [labs](labs/README.md) cover setup, ROS fundamentals, mobile robot and arm simulation, Arabic speech, conversation, GPIO, embedded interfaces, AI models, WhatsApp, and integrated voice home automation.

| Directory | Purpose |
| --- | --- |
| `labs/` | Lab explanations, source, ROS packages, and simulation assets |
| `environments/` | Board and operating system profiles |
| `hardware/` | Parts inventory and wiring requirements |
| `validation/` | Compatibility matrix and test records |
| `docs/` | Course mapping, architecture, roadmap, and lab template |
| `references/` | Source index |
| `.github/` | Issue and pull request templates |

The current source belongs to the GPIO lab. New labs keep their own assets; extract shared components when multiple implemented labs need them.

## Run the first demo

From the repository root on Linux, using Python 3.8 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m arabic_home --command "شغل اللمبة"
python -m arabic_home --command "طفي اللمبة"
```

The phrases mean turn on and turn off the lamp. They display “اللمبة الافتراضية: تعمل” (simulated lamp: on) and “اللمبة الافتراضية: مطفأة” (simulated lamp: off). Each invocation is independent. No state is saved and no audio, GPIO, or ROS is used.

Read the [roadmap](docs/roadmap.md) and [contribution guide](CONTRIBUTING.md). Every lab documents both languages, board differences, hardware, versions, and actual results. A dual board compatibility claim requires recorded runs on both boards.

No reuse license has been selected. The original trainer outline stays local because it contains contact details.

</div>
