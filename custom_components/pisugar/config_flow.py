"""Config flow for PiSugar."""
import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME, CONF_PORT
from homeassistant.helpers import config_validation as cv

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(
            CONF_NAME,
            default="PiSugar",
            description={"suggested_value": "PiSugar", "name": "Name"},
        ): cv.string,
        vol.Required(
            CONF_HOST,
            description={"placeholder": "Enter the host/IP address", "name": "Host"},
        ): cv.string,
        vol.Optional(
            CONF_PORT,
            default=5000,
            description={"placeholder": "Enter the port", "name": "Port"},
        ): cv.port,
    }
)


class PiSugarConfigFlow(config_entries.ConfigFlow, domain="pisugar"):
    """Handle a PiSugar config flow."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_HOST])
            self._abort_if_unique_id_configured()

            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )
