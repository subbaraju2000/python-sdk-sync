# Method: client.media_playback_ids.create()

The `client.media_playback_ids.create()` method allows you to generate a playback ID for a specific media asset. You must provide the `mediaId` of the asset for which you want to generate the playback ID, and you can also configure options such as the `accessPolicy` to control the visibility of the media.

### Parameters Details:

| **Parameter**             | **Description**                                                                                                                             | **Type** | **Accepted Values**                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------------- |
| `mediaId` (required)      | The unique identifier assigned to the media asset. This is required to specify the media for which you want to generate a playback ID.      | `String` | Any valid string (up to 255 characters) |
| `accessPolicy` (required) | Determines if access to the streamed content is kept private or available to all. This can be set to either `public` or `private` or `drm`. | `String` | `"public"`, `"private"`, `"drm"`        |

### Example Request:

```python
# Define the mediaId and accessPolicy dynamically
mediaId =  "media-id" # Unique identifier for the media asset.

playbackOptions = {
  "accessPolicy": "public", # Can be 'public' or 'private'.
}

playbackIdResponse = client.media_playback_ids.create(mediaId, playbackOptions)

print("Playback ID Creation Response:", playbackIdResponse)
```

---

# Method: client.media_playback_ids.delete()

The `client.media_playback_ids.delete()` method allows you to delete a specific playback ID for a media asset. You must provide both the `mediaId` (the unique identifier for the media) and the `playbackId` (the unique identifier for the playback) to delete the playback ID.

### Parameters Details:

| **Parameter**           | **Description**                                                                                      | **Type** | **Accepted Values**                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | -------- | --------------------------------------- |
| `mediaId` (required)    | The unique identifier assigned to the media asset. It can contain a maximum of 255 characters.       | `String` | Any valid string (up to 255 characters) |
| `playbackId` (required) | The unique identifier for the playback ID to be deleted. It can contain a maximum of 255 characters. | `String` | Any valid string (up to 255 characters) |

### Example Request:

```python
# Define the mediaId and playbackId dynamically
mediaId = "media-id"; # The ID of the media asset for which you want to delete the playback ID.
playbackIds = ["id1", "id2"]; # The playback ID that you want to delete.

deletePlaybackResponse = client.media_playback_ids.delete(mediaId, playbackIds)

print("Playback ID Deletion Response:", deletePlaybackResponse)
```
