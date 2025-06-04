from typing import Any, List

from flight_controller_detector.linux.linux_boards import LinuxFlightController
from typedefs import Platform, Serial


class Tummler(LinuxFlightController):
    manufacturer = "Tummler ROV"
    devices = {
        "STM32": (0x66, 1),
    }

    def __init__(self, **data: Any) -> None:
        name = "Tummler"
        plat = Platform.Tummler
        super().__init__(**data, name=name, platform=plat)

    def detect(self) -> bool:
        return all(self.check_for_i2c_device(bus, address) for address, bus in self.devices.values())

    def get_serials(self) -> List[Serial]:
        return [
            Serial(port="C", endpoint="/dev/ttyAMA0"),
            Serial(port="B", endpoint="/dev/ttyAMA2"),
        ]
