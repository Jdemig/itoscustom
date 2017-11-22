import os
import audio
import imagecapture

#os.system('espeak "Hello, welcome to the SoundForBlind device"')

# call image capture.py and array of data 64x64?

image = imagecapture.getImage()
print("Done capturing image")
frequencyArray = []


for x in range(0, 64):
	row = []
	for y in range(0, 64):
		frequency = int(((image[x][y] / 255) * 14000) + 500)
		row.append(frequency)
	frequencyArray.append(row)
print("done appending array")
audio.outputAudio(frequencyArray)




# create a frequncy array that correlates to the array of values [ [B, G, R], [B, G, R] ]
# frequency array then looks like [ 286, 293 ] 286 matching the first BGR array
# pass array to audioout.py




