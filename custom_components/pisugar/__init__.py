"""The pisugar component."""
import logging
import voluptuous as vol

from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType, HomeAssistantType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "pisugar"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_NAME): cv.string,
                vol.Required(CONF_HOST): cv.string,
                vol.Optional(CONF_PORT, default=5000): cv.port,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass: HomeAssistantType, config: ConfigType) -> bool:
    """Set up the pisugar component."""
    hass.data[DOMAIN] = config[DOMAIN]
    return True
