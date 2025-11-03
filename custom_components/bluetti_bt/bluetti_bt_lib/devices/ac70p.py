"""AC70P fields."""

from typing import List

from ..base_devices.ProtocolV2Device import ProtocolV2Device
from ..utils.commands import ReadHoldingRegisters


class AC70P(ProtocolV2Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "AC70P", sn)

    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return self.struct.get_read_holding_registers()
