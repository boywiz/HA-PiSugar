# HA-PiSugar


# Daily Schedule Card

[![HACS Badge](https://img.shields.io/badge/HACS-Default-31A9F4.svg?style=plastic)](https://github.com/hacs/integration)


![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/boywiz/HA-PiSugar?style=plastic)

![Project Maintenance](https://img.shields.io/badge/maintainer-Maurice%20Manning-blue.svg?style=plastic)

## Install

If you use [HACS](https://hacs.xyz/), the custom card will automatically be registered as needed.

If you don't use HACS, you can download js file from [latest releases](https://github.com/amitfin/lovelace-daily-schedule-card/releases/). Follow [these instructions](https://developers.home-assistant.io/docs/frontend/custom-ui/registering-resources) to register the custom card.


HA PiSugar is a custom_component for Home Assistant.

1. The recommended installation method is using [HACS](https://hacs.xyz): search for "Auto Areas", install it and restart Home Assistant.
Alternatively [download a release](https://github.com/c-st/auto_areas/releases) and copy the folder `custom_components/ha-pisugar` to the `custom_components` folder of your Home Assistant installation.


## Configuration

```yaml
# Place this code in your home assistant configuration file (e.g., configuration.yaml)

sensor:
  - platform: pisugar
    instances:
      - name: PiSugar 1
        host: 192.168.1.100
        port: 5000
      - name: PiSugar 2
        host: 192.168.1.101
        port: 5000

```




## Usage

![demo](https://user-images.githubusercontent.com/19599059/212492789-a42c6e4e-a6af-4231-94eb-c01358994bbe.png)

[Usage demo clip](https://user-images.githubusercontent.com/19599059/212492805-c2cf0d27-2ea5-462e-b13f-73010eed1758.mov)