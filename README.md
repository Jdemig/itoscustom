# itoscustom - image to sound custom
itoscustom is a program for for the Raspberry Pi that converts images to into sound bites that are interpretable by the listener. The general idea is that if you create a an algorithm that is able to map pixel brightness to a frequency in a consistent way, then the brain will be plastic enough to learn how to interpret the sound bites and use them to navigate their surroundings.

It first takes a column of pixels and converts the RGB color scheme into BW. We then use the array of black and white values associated with the first column of pixels and superimpose the frequencies onto eachother. Ideally this should create a frequency that can be understood by the listener. You repeat the process until you've created an audio bite for every column and then play the entire sound for the listener. To be clear, we are not superimposing all columns. Only one column of pixel/sound mappings is superimposed and we then play each column one after the other.

This has been done before successfully, however this specific project was never thoroughly tested.
