# Smart Energy Data

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub](https://img.shields.io/github/license/JohnAdders/n3rgy)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/JohnAdders/n3rgy)](https://github.com/JohnAdders/n3rgy/issues)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-brightgreen.svg)](https://github.com/JohnAdders/n3rgy/graphs/commit-activity)

The **n3rgy** component is a Home Assistant custom sensor which provides access to historic energy consumption data and tariff information.

## TABLE OF CONTENTS

* [Installation](#installation)
* [Configuration](#configuration)
  * [Config Flow](#config-flow)
  * [Configuration Parameters](#configuration-parameters)
* [State](#state)

## INSTALLATION

This integration is able to install via HACS.

1. Ensure that [HACS](https://custom-components.github.io/hacs/) is installed.
2. Search for and install the **n3rgy** integration.
3. Configure the **n3rgy** sensor.
4. Restart Home Assistant.

## CONFIGURATION

**n3rgy** can be configured on the integrations menu or in configuration.yaml

### CONFIG FLOW

In Configuration/Integrations click on the **<+>** button, select **n3rgy** and configure the options on the form.

### configuration.yaml

Add **n3rgy** sensor in your `configuration.yaml`.

```yaml
# Example configuration.yaml entry

n3rgy:
  name: 'Consumption Data'
  host: !secret host_url
  api_key: !secret api_key
  property_id: !secret property_id

```

Optional arguments:

```yaml
n3rgy:
  name: 'Consumption Data'
  ...
  environment: true     # live environment enabled
  daily_update: true    # daily update flag
  utility: electricity  # utility type
  start: 202102080130   # start date/time (FORMAT: YYYYMMDDHHmm)
  end: 202102091125     # end date/time (FORMAT: YYYYMMDDHHmm)

```

### CONFIGURATION PARAMETERS

| Parameter | Optional | Description |
|:--------- | -------- | ----------- |
| `name` | Yes | Sensor name |
| `host` | No | The server URL used to call the SDK methods |
| `api_key` | No | The API key used for authentication with the server |
| `property_id` | No | The Property ID, which can be either an MPAN or MPRN |
| `environment` | Yes | Live environment flag (default: `false`) |
| `daily_update` | Yes | Daily update flag (default: `true`) |
| `utility` | Yes | Utility type (default: `electricity`) |
| `start` | Yes | Start date/time of the period in the format YYYYMMDDHHmm |
| `end` | Yes | End date/time of the period in the format YYYYMMDDHHmm |

## STATE

Returns values for the consumption of the specified utility (e.g. electricity, gas) at the property identified by the given MPxN. Unless otherwise specified using optional parameters, returns the consumption values for every half-hour of the previous day. Accepts as optional parameters a start date/time, an end date/time, live environment flag.
