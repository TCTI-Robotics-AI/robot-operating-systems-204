<div dir="rtl" lang="ar">

# حاوية <span dir="ltr">Noetic</span> لمسار <span dir="ltr">Pi 5</span>

يوفر هذا المجلد وصف بناء يستخدم الصورة الرسمية <span dir="ltr">ros:noetic-ros-base-focal</span>، المتاحة لمعمارية <span dir="ltr">arm64.</span> الحاوية تحمل بيئة المنهج القديمة فوق نظام <span dir="ltr">Pi 5</span> الأصلي <span dir="ltr">Ubuntu 24.04.</span> هذا مسار إعداد مقدم للتجربة؛ لم يختبر البناء والتشغيل على جهاز <span dir="ltr">Pi 5</span> فعلي بعد.

ثبت <span dir="ltr">Docker</span> وفق [توثيقه الرسمي](https://docs.docker.com/engine/install/ubuntu/)، ثم نفذ من جذر المستودع:

<div dir="ltr">

```bash
docker build -t course204:noetic -f environments/noetic-container/Dockerfile .
docker run --rm -it --network host   -v "$PWD:/course" -v course204-ws:/course_ws   course204:noetic
```

</div>

داخل الحاوية:

<div dir="ltr">

```bash
cd /course
python3 -m pip install '.[conversation,serial]'
bash tools/build.sh /course_ws
source /course_ws/devel/setup.bash
roslaunch course_mobile gazebo.launch gui:=false
```

</div>

في طرفية مضيف جديدة استخرج اسم الحاوية من <span dir="ltr">docker ps</span>، ثم استخدم <span dir="ltr">docker exec -it</span> بالاسم الفعلي لفتح <span dir="ltr">bash</span>، وحمل /<span dir="ltr">course_ws/devel/setup.bash</span> قبل تشغيل عميل <span dir="ltr">ROS.</span> لا يضيف هذا الإعداد واجهة رسومية للحاوية.

## ربط <span dir="ltr">GPIO</span> والصوت

شغل وكيل <span dir="ltr">GPIO</span> على النظام الأصلي واتصل به من الحاوية على <span dir="ltr">127.0.0.1</span> بفضل <span dir="ltr">network host.</span> [تمرين الرازبيري](../../labs/06-embedded-systems/03-raspberry-pi/README.md) يوضح الإعداد. لا حاجة لوضع <span dir="ltr">privileged.</span> للصوت يمكن تشغيل التعرف على النظام الأصلي ومعالجة ملف <span dir="ltr">WAV</span> داخل الحاوية؛ تمرير الميكروفون ومخرج الصوت مباشرة يحتاج إعدادا واختبارا مستقلين.

للوحات <span dir="ltr">USB</span> استخدم مضيف <span dir="ltr">ROS</span> أصليا أو مرر المنفذ المحدد فقط عبر --<span dir="ltr">device=/dev/ttyACM0</span>، بعد التحقق من اسمه. لا تستخدم هذا المثال لإثبات توافق منافذ لم تختبر.

هذه الحاوية تحافظ على <span dir="ltr">Catkin</span> و<span dir="ltr">Noetic</span>؛ لا تضيف <span dir="ltr">micro-ROS</span> ولا تحول برنامج اللوحة تلقائيا إلى عقدة <span dir="ltr">ROS 2.</span>

</div>

<div dir="ltr" lang="en">

# Noetic container for the Pi 5 path

The Dockerfile uses the official arm64-capable ros:noetic-ros-base-focal image to host the legacy course environment over native Ubuntu 24.04. This is a provided setup path, not a physically validated Pi 5 deployment.

Install Docker using its [official instructions](https://docs.docker.com/engine/install/ubuntu/), then run from the repository root:

```bash
docker build -t course204:noetic -f environments/noetic-container/Dockerfile .
docker run --rm -it --network host   -v "$PWD:/course" -v course204-ws:/course_ws   course204:noetic
```

Inside:

```bash
cd /course
python3 -m pip install '.[conversation,serial]'
bash tools/build.sh /course_ws
source /course_ws/devel/setup.bash
roslaunch course_mobile gazebo.launch gui:=false
```

Use docker ps to find the actual container name, then docker exec -it NAME bash for another terminal and source /course_ws/devel/setup.bash. This configuration is headless.

Run GPIO natively and reach its loopback agent from the host-networked container as described in the [Pi lab](../../labs/06-embedded-systems/03-raspberry-pi/README.md). No privileged mode is needed. Audio can be recorded natively and supplied as a WAV; direct microphone/output passthrough needs separate configuration and validation. For USB boards use a native ROS host or pass only the actual device with --device=/dev/ttyACM0. Do not infer untested device compatibility.

The container retains Catkin/Noetic; it does not add micro-ROS or convert firmware to ROS 2.

</div>
