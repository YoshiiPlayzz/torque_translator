# Torque Translator for HomeAssistant
This Docker container is used for "translating" the logs that are send via torque to this server to an api call to your HomeAssistant instance.
You can use this container if you haven't have an ssl certificate for your HomeAssistant instance.
# Example HomeAssitant config
```yaml
... 
sensor:
  ...
  - platform: torque
    email: "name@example.com"
    name: YourCarName
...
``` 

# Environment variables 
- `EMAIL`: Set the email you have set in the HomeAssistant config 
- `URL`: URL to your HomeAssistant config e.g. `http://@/<homeassistant_ip>:8123`
- `BEARER`: Long-time access token. How to get you can see [here](https://community.home-assistant.io/t/how-to-get-long-lived-access-token/162159)

# Docker commands 
TODO