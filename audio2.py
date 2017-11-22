import pyaudio
import math



def outputAudio(frequency):

	PyAudio = pyaudio.PyAudio

	bitrate = 16000

	length = 1.3

	numberofframes = int(bitrate * length)
	restframes = numberofframes % bitrate
	wavedata = ''

	def superposition(x, y):
		summation = 0
		# for every x and y value get summation of all z range frequncies and return
		for z in range(0, 64):
			summation = summation + int(math.sin(x/((bitrate/frequency[y][z])/(2*3.1415)))*127+128)
		summation = summation / 64
		return summation
	print("done summation")
	a = 0
	# goes through 
	for x in xrange(numberofframes):
		y = int(x/325)
		wavedata = wavedata + chr(superposition(x, y))
		
	print("getting wavedata")

	#fill remainder of frameset with silence
	for x in xrange(restframes): 
		wavedata = wavedata+chr(128)
	print("filled remainder of frameset w/silence")

	p = PyAudio()
	stream = p.open(format = p.get_format_from_width(1),
		channels = 1,
		rate = bitrate,
		output = True)
	stream.write(wavedata)
	stream.stop_stream()
	stream.close()
	p.terminate()