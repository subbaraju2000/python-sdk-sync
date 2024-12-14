# Manage Live Stream Simulcast

Simulcasting allows you to stream your live content to multiple platforms simultaneously, broadening your reach and audience. A suite of methods is available to manage live stream simulcasts, including creating a new simulcast, retrieving its details, updating its configuration, and deleting an existing simulcast. 

To manage simulcasts effectively, you’ll need the `streamId` (generated when you initiate a live stream) and the `simulcastId` (generated when the simulcast is created). These identifiers are crucial for linking simulcast operations to the correct live stream and simulcast.

# Method: client.livestreams.create_simulcast()

The `client.livestreams.create_simulcast()` method allows you to create a new simulcast for an existing live stream. Provide the `streamId` of the live stream and a simulcast payload containing the URL and stream key required to start streaming to third-party platforms.

In the response `simulcastId` must be retained for managing future operations on the simulcast, such as updating or deleting it.

### Parameter Details:

| **Parameter**          | **Description**                                                                                                                                      | **Type** | **Accepted Values**                                           |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------- |
| `url` (required)       | The RTMP URL, combined with the application name, is crucial for connecting to third-party live streaming services and transmitting the live stream. | `String` | Any valid RTMP URL (e.g., `rtmps://live.fastpix.io:443/live`) |
| `streamKey` (required) | A unique stream key that allows the user to start streaming on a third-party platform. This key is used in the RTMP stream configuration.            | `String` | Any valid stream key (max 255 characters)                     |
| `streamId` (required) | The unique identifier assigned to the live stream. This ID is generated during the creation of the live stream. | `String` | Any valid string (max 255 characters) |

### Example Request:

```python
# Define the simulcast payload with the URL and stream key
simulcastPayload = {
    "url": "rtmps://live.fastpix.io:443/live",
    "streamKey": "46c3457fa8a579b2d4da64125a2b6e83ka09f3e958c16ed00e85bfe798abd9845"  # Replace with actual stream key
}

streamId = "a09f3e958c16ed00e85bfe798abd9845"  # Replace with actual stream ID

generateSimulcast = client.livestreams.create_simulcast(streamId, simulcastPayload)

print("Generate Simulcast:", generateSimulcast)
```

---

# Method: client.livestreams.get_simulcast()

The `client.livestreams.get_simulcast()` method allows you to retrieve details of a specific simulcast for a live stream. To use this method, you need to provide both the `streamId` (the unique identifier for the live stream) and the `simulcastId` (the unique identifier for the simulcast stream).

### Parameter Details:

| **Parameter**            | **Description**                                                                                                  | **Type** | **Accepted Values**                   |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------- |
| `streamId` (required)    | The unique identifier assigned to the live stream. This ID is generated during the creation of the live stream.  | `String` | Any valid string (max 255 characters) |
| `simulcastId` (required) | The unique identifier assigned to the simulcast stream. FastPix generates this ID when the simulcast is created. | `String` | Any valid string (max 255 characters) |

### Example Request:

```python
# Define the streamId and simulcastId for the simulcast you want to retrieve
streamId = "a09f3e958c16ed00e85bfe798abd9845"  # Replace with actual stream ID
simulcastId = "7269209ff0299319b6321c9a6e7850ff"  # Replace with actual simulcast ID

getLiveSimulcast = client.livestreams.get_simulcast(streamId, simulcastId)

print("Live Stream Simulcast Details:", getLiveSimulcast)
```

---

# Method: client.livestreams.update_simulcast()

The `client.livestreams.update_simulcast()` method allows you to update the configuration of a simulcast stream for a live stream. To use this method, you need to provide the `streamId` (the unique identifier for the live stream), `simulcastId` (the unique identifier for the simulcast stream), and the fields you wish to update, such as `isEnabled` and `metadata`.

### Parameter Details:

| **Parameter**            | **Description**                                                                                                                          | **Type**  | **Accepted Values**                                             |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------- |
| `streamId` (required)    | The unique identifier assigned to the live stream. This ID is generated during the creation of the live stream.                          | `String`  | Any valid string (max 255 characters)                           |
| `simulcastId` (required) | The unique identifier assigned to the simulcast stream. FastPix generates this ID when the simulcast is created.                         | `String`  | Any valid string (max 255 characters)                           |
| `isEnabled`              | Determines if the simulcast stream is enabled or disabled. Set to `False` to disable the simulcast.                                      | `Boolean` | `True` (enabled), `False` (disabled)                            |
| `metadata`               | Arbitrary user-supplied metadata that will be included in the simulcast details. Max 255 characters per key and value, up to 10 entries. | `Object`  | Any valid key-value pair (max 255 characters per key and value) |

### Example Request:

```python
# Assign streamId, simulcastId, and fields to variables
streamId = "a09f3e958c16ed00e85bfe798abd9845"  # Replace with actual stream ID
simulcastId = "7269209ff0299319b6321c9a6e7850ff"  # Replace with actual simulcast ID

updatePayload = {
    "isEnabled": False,  # Disable the simulcast stream (set to True to enable)
    "metadata": {
        "simulcast2": "media"  # Update the metadata as needed
    }
}

updateLiveSimulcast = client.livestreams.update_simulcast(streamId, simulcastId, updatePayload)

print("Updated Live Stream Simulcast:", updateLiveSimulcast)
```

---

# Method: deleteLiveStreamSimulcast()

The `deleteLiveStreamSimulcast()` method allows you to delete a specific simulcast associated with a live stream. To remove a simulcast, you need to provide both the `streamId` (unique identifier of the live stream) and `simulcastId` (unique identifier of the simulcast) that you want to delete.

### Parameter Details:

| **Parameter**            | **Description**                                                                                             | **Type** | **Accepted Values**                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- | -------- | ------------------------------------- |
| `streamId` (required)    | The unique identifier assigned to the live stream. This ID is generated when the stream is created.         | `String` | Any valid string (max 255 characters) |
| `simulcastId` (required) | The unique identifier assigned to the simulcast stream. This ID is generated when the simulcast is created. | `String` | Any valid string (max 255 characters) |

### Example Request:

```python
# Assign streamId and simulcastId to variables
streamId = "a09f3e958c16ed00e85bfe798abd9845"  # Replace with actual stream ID
simulcastId = "7269209ff0299319b6321c9a6e7850ff"  # Replace with actual simulcast ID

deleteLiveSimulcast = client.livestreams.delete_simulcast(streamId, simulcastId)

print("Deleted Live Stream Simulcast:", deleteLiveSimulcast)
```
