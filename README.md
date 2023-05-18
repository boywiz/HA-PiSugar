# HA Pi Sugar UPS Sensor


# Daily Schedule Card

[![HACS Badge](https://img.shields.io/badge/HACS-Default-31A9F4.svg?style=plastic)](https://github.com/hacs/integration)


![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/boywiz/HA-PiSugar?style=plastic)

![Project Maintenance](https://img.shields.io/badge/maintainer-Maurice%20Manning-blue.svg?style=plastic)

- [Home Assistant (HA) Pi Sugar](#home-assistant-Pi-Sugar)
  - [How to install](#how-to-install)
    - [HACS](#hacs)
    - [Manual](#manual)
  - [How to setup](#how-to-setup)
  - [Target Rate Sensors](#target-rate-sensors)
  - [Services](#services)
  
  //TODO: update this 
       - [Service pisugar\_energy.update\_target\_config](#service-pisugar_energyupdate_target_config)
  - [Energy Dashboard](#energy-dashboard)
  - [Community Contributions](#community-contributions)
  - [FAQ](#faq)
  
## How to install

There are multiple ways of installing the integration.

### HACS

[![HACS Badge](https://img.shields.io/badge/HACS-Default-31A9F4.svg?style=plastic)](https://github.com/hacs/integration)

This integration can be installed directly via HACS. To install:

* [Add the repository](https://my.home-assistant.io/redirect/hacs_repository/?owner=boywiz&repository=[HA-PiSugar](https://github.com/boywiz/HA-PiSugar)&category=integration) to your HACS installation
* Click `Download`

### Manual

You should take the latest [published release](https://github.com/boywiz/HA-PiSugar/releases). The current state of `develop` will be in flux and therefore possibly subject to change.

To install, place the contents of `custom_components` into the `<config directory>/custom_components` folder of your Home Assistant installation. Once installed, don't forget to restart your home assistant instance for the integration to be picked up.

If you use [HACS](https://hacs.xyz/), the custom card will automatically be registered as needed.

If you don't use HACS, you can download js file from [latest releases](https://github.com/amitfin/lovelace-daily-schedule-card/releases/). Follow [these instructions](https://developers.home-assistant.io/docs/frontend/custom-ui/registering-resources) to register the custom card.


HA PiSugar is a custom_component for Home Assistant.

1. The recommended installation method is using [HACS](https://hacs.xyz): search for "Auto Areas", install it and restart Home Assistant.
Alternatively [download a release](https://github.com/c-st/auto_areas/releases) and copy the folder `custom_components/pisugar` to the `custom_components` folder of your Home Assistant installation.


## Configuration

//TODO: No longer needed ned Screen shot
```yaml
# Place this code in your home assistant configuration file (e.g., configuration.yaml)

sensor:
  - platform: pisugar
    instances:
      - name: PiSugar 1
        host: 192.168.1.100
        port: 8423
      - name: PiSugar 2
        host: 192.168.1.101
        port: 8423

```

