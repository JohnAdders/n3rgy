"""
Script file: __init__.py
Created on: Jan 29, 2021
Last modified on: Feb 3, 2021

Comments:
    n3rgy data API integration

Notes:
    This API was not published to PyPI store yet
    We can use simple request function
"""

import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.exceptions import ConfigEntryNotReady
from .const import (
    DOMAIN,
    PLATFORM
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """
    Old way of setting up n3rgy component using YAML
    :param hass: home assistant object
    :param config: config file
    :return: true (expired)
    """
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """
    Set up n3rgy component from a config entry
    :param hass: home assistant object
    :param entry: config entry
    :return: true if successful
    """
    # add sensor
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, PLATFORM)
    )
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """
    Unload a config entry
    :param hass: home assistant object
    :param entry: config entry
    :return: true if successful, false otherwise
    """
    # remove config entry
    try:
        await hass.config_entries.async_forward_entry_unload(entry, PLATFORM)
        _LOGGER.info("Successfully removed sensor from the n3rgy integration!")
        return True
    except ValueError as ex:
        _LOGGER.error(f"Failed to remove sensor: {str(ex)}")
        return False
