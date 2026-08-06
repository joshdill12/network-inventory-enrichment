from dataclasses import dataclass, field

"""
Common data model representing a discovered network device.

The inventory module populates the required fields.
The discovery modules enrich this object with additional data.
"""

@dataclass(slots=True)
class Device:
    hostname: str
    ip: str
    vendor: str

    model: str | None = None
    serial: str | None = None
    version: str | None = None

    interfaces: list = field(default_factory=list)
    neighbors: list = field(default_factory=list)
