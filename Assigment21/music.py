import pysynth as ps
mosi = (('f', 4), ('b', -1), ('d', 4),
		('c5', -2), ('e6', 8), ('d#6', 2),
		('d#6', 4), ('e#4', 4), ('g', 4),
		('c5', -2), ('e6', 8), ('d#6', 2))
ps.make_wav(mosi, fn = "mosi1.wav")