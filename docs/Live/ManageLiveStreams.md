# Managing Live Streams

Live streams are uniquely identified by the `streamId`, which is generated automatically when you create a new live stream using the `client.livestreams.create()` method. This `streamId` is essential for performing any operations related to live streams, such as retrieving details, updating configurations, or deleting streams.

---

# Method: client.livestreams.list()

The `client.livestreams.list()` method allows you to fetch a list of all live streams. You can customize the query by modifying parameters such as `limit`, `offset`, and `orderBy`. If no parameters are provided, the method will use default values.

### Parameter Details:

The method accepts the following query parameters:

| **Parameter** | **Description**                                                                       | **Type** | **Default Value** | **Accepted Values**                         |
| ------------- | ------------------------------------------------------------------------------------- | -------- | ----------------- | ------------------------------------------- |
| `limit`       | Specifies the maximum number of items to display per page.                            | `Number` | `10`              | 1 to 50                                     |
| `offset`      | Determines the starting point for data retrieval in a paginated list.                 | `Number` | `1`               | Any positive integer (e.g., `1`, `5`, `10`) |
| `orderBy`     | Sorts the list of streams. The list can be arranged in ascending or descending order. | `String` | `desc`            | `"desc"`, `"asc"`                           |

### Example Request:

```python
# Define pagination settings for retrieving live streams
getAllLiveStreamPagination = {
  "limit": 10, # Limit the number of live streams retrieved.
  "offset": 1, # Skip a specified number of streams for pagination.
  "orderBy": "asc", # Order the results based on the specified criteria ("asc" or "desc").
}

const getAllLiveStreams = client.livestreams.list(getAllLiveStreamPagination)
print("All Live Streams:", getAllLiveStreams)
```

---

# Method: client.livestreams.get()

The `client.livestreams.get()` method allows you to retrieve the details of a specific live stream by its unique stream ID. After initiating a live stream, FastPix assigns a unique identifier to the stream, which can be used to fetch its details.

### Parameter Details:

| **Parameter**         | **Description**                                                                              | **Type** | **Accepted Values**                   |
| --------------------- | -------------------------------------------------------------------------------------------- | -------- | ------------------------------------- |
| `streamId` (required) | The unique identifier assigned to the live stream. You receive this ID upon stream creation. | `String` | Any valid string (max 255 characters) |

### Example Request:

```python
# Define the streamId for the live stream you want to retrieve
streamId =  "a09f3e958c16ed00e85bfe798abd9845" # Replace with actual stream ID
getLiveStreamById = client.livestreams.get(streamId)

print("Live Stream Details:", getLiveStreamById)
```

---

# Method: client.livestreams.update()

The `client.livestreams.update()` method allows you to update the configuration of a live stream. You can modify various settings, such as metadata and reconnect window, using this method. To apply updates, provide the `streamId` of the stream you wish to modify and specify the fields you want to update.

### Parameter Details:

| **Parameter**                | **Description**                                                                                                                                                   | **Type**  | **Accepted Values**                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------- |
| `streamId` (required)        | The unique identifier assigned to the live stream. You receive this ID upon stream creation.                                                                      | `String`  | Any valid string (max 255 characters)                           |
| `metadata` (optional)        | Optional metadata to tag the live stream with key-value pairs. You can add up to 10 key-value pairs, and each key and value can have a maximum of 255 characters. | `Object`  | Any valid key-value pair (max 255 characters per key and value) |
| `reconnectWindow` (optional) | The time (in seconds) before ending the stream in case of a disruption. This value can range from 60 to 1800 seconds.                           | `Integer` | 60 to 1800 (seconds)                                            |

### Example Request:

```python
# Define the fields to be updated in the live stream configuration
streamId = "a09f3e958c16ed00e85bfe798abd9845" # Provide the stream ID for the live stream to update
updateLiveStreamRequest = {
  "metadata": {
    "livestream_name": "Game_streaming",
  },
  "reconnectWindow": 100,
}

updateLiveStream = client.livestreams.update(streamId,updateLiveStreamRequest)

print("Updated Live Stream:", updateLiveStream)
```

---

# Method: client.livestreams.delete()

The `client.livestreams.delete()` method allows you to delete a live stream by its unique `streamId`. To remove a stream, provide the `streamId` of the stream you wish to delete. This method permanently deletes the live stream and all associated data.

### Parameter Details:

| **Parameter**         | **Description**                                                                                       | **Type** | **Accepted Values**                   |
| --------------------- | ----------------------------------------------------------------------------------------------------- | -------- | ------------------------------------- |
| `streamId` (required) | The unique identifier assigned to the live stream. You receive this ID when creating the live stream. | `String` | Any valid string (max 255 characters) |

### Example Request:

```python
# Define the streamId for the live stream you wish to delete
streamId = "a09f3e958c16ed00e85bfe798abd9845" # Provide the stream ID for the live stream to delete
deleteLiveStream = client.livestreams.delete(streamId)
print("Deleted Live Stream:", deleteLiveStream)
```
