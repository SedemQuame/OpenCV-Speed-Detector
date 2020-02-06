"""
Description: A python script, responsible for uploading image/video capture to the cloudinary storage platform,
and returning some meta data such as the url at which the asset is stored at.
Author: Sedem Quame Amekpewu
Date: Monday, 3rd February, 2020
"""

# modules
import json
import keys
import cloudinary
import cloudinary.uploader
import cloudinary.api
import uuid

class assetUploader:
    def __init__(self, keys, video_url):
        self.keys = keys
        self.video_local_url = video_url
    
    def generateUUID(self):
        uui = uuid.uuid4()
        return("video_" + str(uui.hex))

    def cloudinaryUploader(self):    
        uuid = self.generateUUID()

        cloudinary.config( 
        cloud_name = json.loads(self.keys.json_string)["CLOUDINARY_NAME"], 
        api_key = json.loads(self.keys.json_string)["CLOUDINARY_KEY"], 
        api_secret = json.loads(self.keys.json_string)["CLOUDINARY_SECRET"]
        )

        response = cloudinary.uploader.upload_large(self.video_local_url, 
        resource_type = "video",
        public_id = "maakye_wo/" + uuid,
        chunk_size = 6000000,
        eager = [
            { "width": 300, "height": 300, "crop": "pad", "audio_codec": "none"},
            { "width": 160, "height": 100, "crop": "crop", "gravity": "south",
                "audio_codec": "none"}],
        #   eager_async = true,
        eager_notification_url = "https://mysite.example.com/notify_endpoint")
        return(response)


# Getting the url, of the uploader video asset.
# uploadedVideoUrl = assetUploader(keys).cloudinaryUploader()
# print(uploadedVideoUrl)