<div dir="rtl" lang="ar">

# البدء وتشغيل تمارين المقرر

اقرأ [فهرس البنود](exercises-index.md) لاختيار التمرين. الشرح والكود لا يغنيان عن قياس نتيجة التنفيذ. تعتمد تمارين المنهج <span dir="ltr">Catkin</span> و<span dir="ltr">ROS 1 Noetic</span> و<span dir="ltr">Gazebo Classic 11</span>؛ انتهى دعم هذه البيئة ويحتفظ بها لأغراض المقرر. مسار <span dir="ltr">ROS 2</span> أو <span dir="ltr">micro-ROS</span> ليس بديلا تلقائيا لها.

## اختيار بيئة التشغيل

- <span dir="ltr">Pi 4: Ubuntu 20.04 arm64</span> مع <span dir="ltr">Noetic</span> على النظام مباشرة، أو استخدام مضيف <span dir="ltr">ROS</span> منفصل.
- <span dir="ltr">Pi 5: Ubuntu 24.04 arm64</span> للنظام الأصلي، مع [حاوية Noetic](../environments/noetic-container/README.md) أو مضيف <span dir="ltr">ROS</span> منفصل. يعمل <span dir="ltr">GPIO</span> والصوت على النظام الأصلي عند الحاجة.
- حاسب المتدرب: <span dir="ltr">Ubuntu 20.04 amd64</span> أو <span dir="ltr">WSL</span> بهذا الإصدار لتجارب <span dir="ltr">ROS</span> والمحاكاة. وجود شاشة ودعم رسوميات مطلوب لأدوات العرض التفاعلية؛ الاختبارات المحلية المثبتة تستخدم المحاكاة دون واجهة رسومية.

أوامر التثبيت المباشر في الوحدة الثانية مخصصة لبيئة <span dir="ltr">Ubuntu 20.04.</span> لا تنفذها على النظام الأصلي للرازبيري الخامس.

## تنزيل المشروع وبناء الحزم

<div dir="ltr">

```bash
git clone https://github.com/TCTI-Robotics-AI/robot-operating-systems-204.git
cd robot-operating-systems-204
python3 tools/diagnose.py
# Ubuntu 20.04 only: review plans, then apply using a sudo-capable account
bash labs/02-installation-and-setup/01-ubuntu-repositories/configure-apt.sh --apply
bash labs/02-installation-and-setup/02-ros-installation/install-noetic.sh --apply
source /opt/ros/noetic/setup.bash
python3 -m pip install --user '.[conversation,serial]'
python3 tools/workspace.py --workspace ~/course204_ws
bash labs/02-installation-and-setup/03-rosdep-and-environment/initialize.sh ~/course204_ws
bash tools/build.sh ~/course204_ws
source ~/course204_ws/devel/setup.bash
```

</div>

تثبيت مكتبات <span dir="ltr">Python</span> أعلاه يستخدم <span dir="ltr">Python</span> النظام على <span dir="ltr">Ubuntu 20.04</span> لكي تجدها عقد <span dir="ltr">Catkin.</span> لا تشغل البناء من بيئة <span dir="ltr">Python</span> معزولة بإصدار مختلف. أدوات تجميع المتحكمات لها بيئة منفصلة موضحة في تمرين <span dir="ltr">Arduino.</span>

## أول اختبار <span dir="ltr">ROS</span>

شغل الخادم في الطرفية الأولى واتركه يعمل. افتح طرفية ثانية وحمل بيئة منطقة العمل قبل استدعاء الخدمة.

<div dir="ltr">

```bash
# Terminal 1
source ~/course204_ws/devel/setup.bash
roslaunch course_devices lamp.launch backend:=mock
```

</div>

<div dir="ltr">

```bash
# Terminal 2
source ~/course204_ws/devel/setup.bash
rosservice call /lamp/set "on: true"
rostopic echo -n 1 /lamp/state
rostopic echo -n 1 /lamp/simulated
rosservice call /lamp/set "on: false"
```

</div>

الحالة الافتراضية <span dir="ltr">true</span> في /<span dir="ltr">lamp/simulated</span> تميز المحاكاة. استبدل السائق فقط عند الانتقال إلى لوحة فعلية. لا تستنتج نجاح جهاز من وجود رسالة أمر.

## تشغيل المحاكاة

<div dir="ltr">

```bash
# Terminal 1; stop any previous simulation first
roslaunch course_mobile gazebo.launch gui:=false
```

</div>

<div dir="ltr">

```bash
# Terminal 2, after sourcing the workspace
rosrun course_mobile drive.py --linear 0.1 --seconds 3
rostopic echo -n 1 /odom
```

</div>

ابدأ بتمارين المتنقل، ثم الذراع، ثم المحادثة والأنظمة المدمجة. لا تشغل نموذجي المتنقل والذراع معا ضمن الإعداد الافتراضي؛ يشتركان في وصف الروبوت وعالم <span dir="ltr">Gazebo.</span>

## ماذا تسلم؟

نسخة الكود المستخدمة، وموديل الجهاز والمعمارية والنظام، والإصدارات، والأوامر والملاحظات، وسجل نتائج النجاح والفشل. كل تمرين يتضمن تطبيقا إضافيا وأساليب تحقق. تقارير الحاسب في [التحقق](../validation/README.md) لا تثبت نجاح قطع لم توصل بعد.

</div>

<div dir="ltr" lang="en">

# Getting started with the course labs

Use the [syllabus item index](exercises-index.md) to select a lesson. The course retains legacy ROS 1 Noetic, Catkin and Gazebo Classic 11. Their support has ended; do not silently replace them with ROS 2 or micro-ROS.

Pi 4 targets native Ubuntu 20.04 arm64/Noetic or a separate ROS host. Pi 5 targets native Ubuntu 24.04 arm64 plus the [Noetic container](../environments/noetic-container/README.md) or a separate ROS host. GPIO/audio run natively when needed. Ubuntu 20.04 amd64 or WSL can run the software labs. Interactive visualization needs suitable graphics; recorded local tests use headless simulation.

## Clone, install and build

Run the following only on a dedicated Ubuntu 20.04 course host; review the installation helper plans before applying. A sudo-capable account is needed for system packages.

```bash
git clone https://github.com/TCTI-Robotics-AI/robot-operating-systems-204.git
cd robot-operating-systems-204
python3 tools/diagnose.py
bash labs/02-installation-and-setup/01-ubuntu-repositories/configure-apt.sh --apply
bash labs/02-installation-and-setup/02-ros-installation/install-noetic.sh --apply
source /opt/ros/noetic/setup.bash
python3 -m pip install --user '.[conversation,serial]'
python3 tools/workspace.py --workspace ~/course204_ws
bash labs/02-installation-and-setup/03-rosdep-and-environment/initialize.sh ~/course204_ws
bash tools/build.sh ~/course204_ws
source ~/course204_ws/devel/setup.bash
```

The Python install uses the Ubuntu 20.04 system interpreter so generated Catkin scripts can find dependencies. Do not build using an unrelated isolated Python version. Firmware compilation uses a separate tools environment described in the Arduino lab.

## First ROS test

Keep terminal 1 running. In terminal 2, source the workspace before calling the service.

```bash
# Terminal 1
source ~/course204_ws/devel/setup.bash
roslaunch course_devices lamp.launch backend:=mock
```

```bash
# Terminal 2
source ~/course204_ws/devel/setup.bash
rosservice call /lamp/set "on: true"
rostopic echo -n 1 /lamp/state
rostopic echo -n 1 /lamp/simulated
rosservice call /lamp/set "on: false"
```

The simulated flag must remain explicit. Switch drivers only when using real hardware. A published command alone is not evidence of actuation.

## First simulation

```bash
# Terminal 1; stop previous simulations first
roslaunch course_mobile gazebo.launch gui:=false
```

```bash
# Terminal 2, after sourcing
rosrun course_mobile drive.py --linear 0.1 --seconds 3
rostopic echo -n 1 /odom
```

Work through mobile, arm, conversation and embedded lessons. Do not launch mobile and arm simultaneously with their default configuration: they share Gazebo and robot_description.

Submit source revision, board/architecture/OS, versions, commands, observations and pass/fail records. Each lesson includes an extension task. [Local software evidence](../validation/README.md) does not validate disconnected physical devices.

</div>
