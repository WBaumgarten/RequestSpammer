# Usage
# RequestSpammer.py URL [options]
# use --help for option usage 

import requests 
import sys
import time
import optparse

def Main():
    url = GetUrlFromArguments()

    parser = optparse.OptionParser("%prog URL [options]")
    parser.add_option("-r", "--repetitions", action="store", type="int", dest="repetitions", default="7", help="The amount of times the request will be sent")

    (options, args) = parser.parse_args()
    SpamRequests(url, options.repetitions)

def SpamRequests(url, numOfRepetitions):
    s = requests.session();
    start = time.time()
    for i in range(numOfRepetitions):
        r = s.post(url = url, headers = GetHeaders())
        try:
            data = r.json()
            print ("{}: #{} - {}".format(round(time.time() - start, 1), i + 1, data))
        except:
            print ("{}: #{} - {}".format(round(time.time() - start, 1), i + 1, r))

def GetUrlFromArguments():
    if (len(sys.argv) < 2):
        print("Supply a URL\nUsage: RequestSpammer.py URL [options]")
        sys.exit()
    return sys.argv[1]

def GetHeaders():
    # The User-Agent should always be set
    return {'User-Agent':'RequestSpammer.py'}

if (__name__ == "__main__"):
    try:
        Main()
    except KeyboardInterrupt:
        print("Stopped sending requests")
        sys.exit()
