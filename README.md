# arena-electronics

# Other Repos

UI / Webserver - https://github.com/fubarlabs/RobotCombatOverlay
ESP32 Firmware - https://github.com/GSCRL/bot-arena-control
## Build Arg Notes

```ini
check_skip_packages = yes
lib_deps = bblanchon/ArduinoJson
build_flags = -O2 -D DEBUG_ESP_PORT=Serial
build_unflags = -Os
```

# Broker Setup

```
allow_anonymous true

listener 1883
protocol mqtt

listener 9001
protocol websockets
```