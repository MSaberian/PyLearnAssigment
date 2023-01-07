import pytube

Link = 'https://www.youtube.com/watch?v=lVFNRrL79w0'
first_stream = pytube.YouTube(Link).streams.first()
first_stream.download(output_path='./',filename= 'test.mp4')