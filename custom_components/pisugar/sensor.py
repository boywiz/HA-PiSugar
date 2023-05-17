"""Support for PiSugar sensors."""
import logging
import socket

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
    CONF_PORT,
    DEVICE_CLASS_BATTERY,
    PERCENTAGE,
)
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "PiSugar"
DEFAULT_PORT = 5000

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
    }
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the PiSugar sensor."""
    name = config.get(CONF_NAME)
    host = config.get(CONF_HOST)
    port = config.get(CONF_PORT)

    async_add_entities([PiSugarSensor(name, host, port)], True)


class PiSugarSensor(Entity):
    """Representation of a PiSugar sensor."""

    def __init__(self, name, host, port):
        """Initialize the PiSugar sensor."""
        self._name = name
        self._host = host
        self._port = port
        self._state = None
        self._available = False

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique ID for the sensor."""
        return f"{self._host}:{self._port}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_class(self):
        """Return the class of the sensor."""
        return DEVICE_CLASS_BATTERY

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of the sensor."""
        return PERCENTAGE

    @property
    def available(self):
        """Return True if the sensor is available."""
        return self._available

    async def async_update(self):
        """Fetch the latest state of the sensor."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((self._host, self._port))
                s.sendall(b"GET")
                data = s.recv(1024)
                self._state = int(data)
                self._available = True
        except (socket.timeout, ConnectionRefusedError, OSError) as err:
            _LOGGER.error("Error reading PiSugar data: %s", err)
            self._state = None
            self._available = False
