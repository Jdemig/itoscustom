import cv2
import picamera
import picamera.array

def getImage():
	with picamera.PiCamera() as camera:
		with picamera.array.PiRGBArray(camera) as stream:
			camera.resolution = (64, 64)

			camera.capture(stream, 'bgr', use_video_port=True)
			# stream.array now contains the image data in BGR order
			grayscaleArray = []
			for x in range(0, 64):
				row = []
				for y in range(0, 64):
					array = stream.array[x][y].tolist()
					grayscale = (array[0]*0.114 + array[1]*0.587 + array[2]*0.299)
					row.append(grayscale)
				grayscaleArray.append(row)
			return grayscaleArray

			#reset the stream before the next capture
			stream.seek(0)
			stream.truncate()

