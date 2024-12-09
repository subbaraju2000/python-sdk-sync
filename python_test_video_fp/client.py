import base64
from .exceptions import APIError
from .signing_keys import SigningKeysResource
from .media import MediaResource
from .playback_ids import MediaPlaybackIDs
from .playback_ids import LivestreamPlaybackIDs
from .live_streams import Livestream
from .api import make_request

class VideoSDKClient:
    def __init__(self, username=None, password=None, api_key=None):
        """
        Initialize the client with flexible authentication.
        
        Args:
            username (str, optional): Username for authentication
            password (str, optional): Password for authentication
            api_key (str, optional): Pre-generated base64 encoded API key
        """

        # Validate and prepare API key
        if api_key:
            self.api_key = api_key
        elif username and password:

            # Encode credentials to base64
            credentials = f"{username}:{password}"
            self.api_key = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        else:
            raise ValueError("Must provide either username and password or a pre-generated API key")
        
        # Prepare headers
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Basic {self.api_key}",
        }
        
        # Initialize resources
        self.signing_keys = SigningKeysResource(self)
        self.media = MediaResource(self)
        self.media_playback_ids = MediaPlaybackIDs(self)
        self.livestream_playback_ids = LivestreamPlaybackIDs(self)
        self.livestreams = Livestream(self)

        # Validate credentials
        self._validate_credentials()

    def _validate_credentials(self):
        """
        Validate credentials by attempting to fetch media.
        Raises an APIError if authentication fails.
        """
        try:
            # Attempt to fetch media to verify credentials
            response = self.media.get_all()
            return response

        except APIError as e:
            raise APIError(f"Authentication failed: {str(e)}") from e
            