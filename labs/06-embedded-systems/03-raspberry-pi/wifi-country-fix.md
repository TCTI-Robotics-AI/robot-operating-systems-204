# إصلاح رفض إعداد دولة الواي فاي | Wi-Fi country-setting repair

<div dir="rtl">

تم اختبار هذا الإصلاح على جهاز Raspberry Pi 5 واحد بتاريخ 2026-10-24، بنظام Ubuntu 24.04.5 وواجهة لاسلكية مدمجة. نطاق التحقق هو اتصال بتردد 2.4 GHz، وليس جميع أجهزة المتدربين أو شبكات 5 GHz.

كانت السجلات تعرض `Firmware rejected country setting` وأخطاء `set chanspec` رغم ضبط الدولة على السعودية. اختبار الإعداد العالمي `00` لم يحل الأخطاء بعد إعادة التشغيل، ولذلك أعيد الإعداد الصحيح `SA`.

نجح تحديث ملف بيانات القنوات والدول `CLM` وحده من مستودع الشركة المصنعة Infineon، مع إبقاء برنامج Ubuntu الأصلي بالإصدار `7.45.234`. أما استبدال البرنامج والملف معا بالإصدار `7.45.286` فأوقف الاتصال بالراوتر في هذا الاختبار، ولذلك تم التراجع عنه.

لم تستبدل ملفات حزم Ubuntu. وضعت نسختان من ملف CLM في مجلد تحديثات البرامج الثابتة، وهو مسار له أولوية التحميل. بقيت بيانات الشبكة وكلمة مرورها كما هي. كما ثبت حد إرسال محافظ قدره 20 dBm بخدمة محلية تبدأ عند توفر الواجهة اللاسلكية.

نجح الاتصال بالإنترنت بعد إعادة التشغيل، ثم نجح بحث جديد عن الشبكات دون ظهور أخطاء الدولة أو القنوات في سجل الإقلاع الجديد. ظهرت قدرة الإرسال 20 dBm، وبقي الاتصال يستخدم WPA2-PSK مع CCMP. هذا تحقق وظيفي محدود، وليس اعتمادا تنظيميا لملف CLM العام أو إثباتا لتوافق جميع الشبكات.

</div>

## Recorded configuration

| Item | Value |
| --- | --- |
| Board | Raspberry Pi 5 Model B Rev 1.0 |
| OS / kernel | Ubuntu 24.04.5 LTS / 6.8.0-1065-raspi, aarch64 |
| Configured country | SA |
| Firmware retained | 7.45.234, FWID 01-996384e2 |
| CLM vendor revision | `d24c95cce5e77b04736972ba05ccd06da6cc377f` |
| CLM SHA-256 | `8fbe9fc2952e2fbab062a142c1ea3e261cd74604761e12f304781b911df4a328` |
| Tested wireless link | 2.4 GHz, channel 6, 20 MHz |
| Transmit limit | 20 dBm, applied by `course204-wifi-txpower.service` |

Only the CLM data was updated. The installed package-owned firmware binary and network credentials were preserved. The full vendor firmware replacement failed association in this environment and was rolled back. This is a device-specific repair record; do not install it automatically on every learner device. The generic vendor CLM is not evidence of Raspberry Pi-specific regulatory certification. Only the recorded 2.4 GHz connection was tested.

Override files on the tested device:

```text
/lib/firmware/updates/brcm/brcmfmac43455-sdio.clm_blob
/lib/firmware/updates/brcm/brcmfmac43455-sdio.raspberrypi,5-model-b.clm_blob
/etc/systemd/system/course204-wifi-txpower.service
```

## Verification | التحقق

Run after a reboot, then repeat after a Wi-Fi scan. The error search should print no matching lines; HTTP should return success. Keep hostnames, network credentials and SSIDs out of published reports.

```bash
sudo wpa_cli -i wlan0 get country
sudo dmesg | grep -E 'Firmware rejected country setting|set chanspec.*fail'
sudo iw dev wlan0 info | grep -E 'channel |txpower'
systemctl is-active course204-wifi-txpower.service
curl -I --max-time 15 https://ubuntu.com
sudo wpa_cli -i wlan0 scan
```

The tested results were `SA`, no matching kernel errors, 20 dBm, an active power-limit service, HTTP 200, and a successful scan. Four consecutive laptop-to-device reachability checks also passed. GPIO outputs were not activated.

## Revert | التراجع

Use a local console or a wired connection before reverting. These commands remove only the two added CLM overrides and the added power-limit service, then reboot into the package-provided firmware configuration. The original package files remain installed.

```bash
sudo rm -f -- /lib/firmware/updates/brcm/brcmfmac43455-sdio.clm_blob \
  /lib/firmware/updates/brcm/brcmfmac43455-sdio.raspberrypi,5-model-b.clm_blob
sudo systemctl disable --now course204-wifi-txpower.service
sudo rm -f -- /etc/systemd/system/course204-wifi-txpower.service
sudo systemctl daemon-reload
sudo reboot
```

## Sources | المصادر

- [Raspberry Pi issue and maintainer discussion of CLM data](https://github.com/raspberrypi/linux/issues/6669).
- [Infineon firmware repository at the tested revision](https://github.com/Infineon/ifx-linux-firmware/tree/d24c95cce5e77b04736972ba05ccd06da6cc377f).
- [Vendor license](https://github.com/Infineon/ifx-linux-firmware/blob/d24c95cce5e77b04736972ba05ccd06da6cc377f/LICENCE). Firmware binaries are not redistributed in this course repository.
