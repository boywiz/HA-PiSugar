# Place this code in a Python file inside the custom_components/pisugar/ directory in your home assistant configuration folder.

import logging
import socket
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_NAME,
    CONF_HOST,
    CONF_PORT,
    PERCENTAGE,
    DEVICE_CLASS_BATTERY,
)
from homeassistant.helpers.entity import Entity

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


def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    host = config.get(CONF_HOST)
    port = config.get(CONF_PORT)

    add_entities([PiSugarSensor(name, host, port)], True)


class PiSugarSensor(Entity):
    def __init__(self, name, host, port):
        self._name = name
        self._host = host
        self._port = port
        self._state = None
        self._available = False

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return f"{self._host}:{self._port}"

    @property
    def state(self):
        return self._state

    @property
    def device_class(self):
        return DEVICE_CLASS_BATTERY

    @property
    def unit_of_measurement(self):
        return PERCENTAGE

    @property
    def available(self):
        return self._available

    def update(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((self._host, self._port))
                s.sendall(b"GET")
                data = s.recv(1024)
                self._state = int(data)
                self._available = True
        except (socket.timeout, ConnectionRefusedError, OSError) as err:
            _LOGGER.error("Error reading Pi Sugar data: %s", err)
            self._state = None
            self._available = False
