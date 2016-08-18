import time
i = 37000
while True:	
	out = open('AVS2.m3u8', "wb")
	out.write("#EXTM3U\n")
	out.write("#EXT-X-VERSION:3\n")
	out.write("#EXT-X-TARGETDURATION:10\n")
	out.write("#EXT-X-MEDIA-SEQUENCE:" + str(i) + "\n")
    	
	out.write("#EXTINF:10.000000,\n")
    	out.write("AVS" + str(i) + ".ts\n")
	out.write("#EXTINF:10.000000,\n")
        out.write("AVS" + str(((i + 1 - 37000) % 239) + 37000) + ".ts\n")
	out.write("#EXTINF:10.000000,\n")
        out.write("AVS" + str(((i + 2 - 37000) % 239) + 37000) + ".ts\n")
	out.write("#EXTINF:10.000000,\n")
        out.write("AVS" + str(((i + 3 - 37000) % 239) + 37000) + ".ts\n")
	out.write("#EXTINF:10.000000,\n")
        out.write("AVS" + str(((i + 4 - 37000) % 239) + 37000) + ".ts\n")
	out.close()
	if i == 37238:
		i = 37000
	else: 
		i = i + 1
	time.sleep(5)
