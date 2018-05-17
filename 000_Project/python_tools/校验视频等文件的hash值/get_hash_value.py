import hashlib

m = hashlib.md5() # test
with open('test_video.mp4',mode='rb') as f: # test_video.mp4为测试用的视频文件，放在执行文件的同级目录
    # for line in f:    # => 45dedcf3a27fb861bfdbf0bb48cab7fd
    #     m2.update(line)

    m.update(f.read())  # => 45dedcf3a27fb861bfdbf0bb48cab7fd
print('test_video.mp4\'s hash value: ',m.hexdigest())