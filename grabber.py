import urllib2
import thread
import time

def Downloder(url, dest):
    ts = urllib2.urlopen(url)
    out = open(dest, "wb")
    out.write(ts.read())
    print('finish downloading ' + dest)
    thread.exit_thread()

if __name__ == '__main__':
    url = 'http://103.10.85.100/hls/'
    lasttimestamp = ""
    firsttimestamp = ""
    i = 0
    total_ts = 720
    while i < total_ts:
        f = urllib2.urlopen(url + 'AVS2.m3u8')
        data = str(f.read())
        arr = data.split('\n')
        timestamp = arr[3].split(':')[1]
        if i == 0:
            firsttimestamp = timestamp
        tsfilename = arr[5]
        print("the timestamp is " + timestamp)
        if cmp(timestamp, lasttimestamp):
            lasttimestamp = timestamp
            thread.start_new_thread(Downloder, (url + tsfilename, 'AVS' + timestamp + '.ts'))
            i += 1
        time.sleep(1)

    out = open('AVS2.m3u8', "wb")
    out.write("#EXTM3U\n")
    out.write("#EXT-X-VERSION:3\n")
    out.write("#EXT-X-TARGETDURATION:10\n")
    out.write("#EXT-X-MEDIA-SEQUENCE:" + firsttimestamp + '\n')
    i = 0
    while i < total_ts:
        out.write("#EXTINF:10.000000,\n")
        out.write("AVS" + str(int(firsttimestamp) + i) + ".ts\n")
        i += 1







