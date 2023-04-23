import speedtest

def printCurrentSpeed():
    test = speedtest.Speedtest()
    print(test.get_best_server()['url'])
    print(test.get_best_server())
    download = int(test.download()/1024/1024)
    print(f'download speed : {download} Mb')
    upload = int(test.upload() / 1024 / 1024)
    print(f'upload speed : {upload} Mb')