import json

keys = {
    "MONGO_URL": "mongodb:#maakye_wo:Z4KemSrIO1VyojtA@cluster0-shard-00-00-x4sv8.mongodb.net:27017,cluster0-shard-00-01-x4sv8.mongodb.net:27017,cluster0-shard-00-02-x4sv8.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority",
    "TEST_URL": "mongodb:#localhost:27017",
    "CLOUDINARY_NAME": "dqv3zrm7e",
    "CLOUDINARY_KEY": "951349685261825" ,
    "CLOUDINARY_SECRET": "E2RWEKKu_fkWiaakpWyic4XFcyk",
    "CLOUDINARY_URL":"cloudinary:#951349685261825:E2RWEKKu_fkWiaakpWyic4XFcyk@dqv3zrm7e",
	# maximum consecutive frames a given object is allowed to be
	# marked as "disappeared" until we need to deregister the object
	# from tracking
	"max_disappear": 10,
	# maximum distance between centroids to associate an object --
	# if the distance is larger than this maximum distance we'll
	# start to mark the object as "disappeared"
	"max_distance": 175,
	# number of frames to perform object tracking instead of object
	# detection
	"track_object": 4,
	# minimum confidence
	"confidence": 0.4,
	# frame width in pixels
	"frame_width": 400,
	# dictionary holding the different speed estimation columns
	"speed_estimation_zone": {"A": 120, "B": 160, "C": 200, "D": 240},
	# real world distance in meters
	"distance": 16,
	# speed limit in mph
	"speed_limit": 1,
	# flag indicating if the frame must be displayed
	"display": True,
	# path the object detection model
	"model_path": "MobileNetSSD_deploy.caffemodel",
	# path to the prototxt file of the object detection model
	"prototxt_path": "MobileNetSSD_deploy.prototxt",
	# flag used to check if dropbox is to be used and dropbox access
	# token
	"use_dropbox": False,
    "use_cloudinary": True,
	"dropbox_access_token": "YOUR_DROPBOX_APP_ACCESS_TOKEN",
	# output directory and csv file name
	"output_path": "output",
	"csv_name": "log.csv"
}

json_string = json.dumps(keys) 