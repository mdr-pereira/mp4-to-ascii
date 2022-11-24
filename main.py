from ffprobe import FFProbe
import ffmpeg
import numpy as np

max_chars_col = 236

def decode_pix(width, height):
    pix_per_char = 10

    disp_ratio = round(width/height, 2)



def main():
    in_filename = 'teapot.mp4'

    metadata = FFProbe(in_filename)
    
    width = -1
    height = -1

    for stream in metadata.streams:
        if stream.is_video():
            width = int(stream.width)
            height = int(stream.height)
    
    process = (
        ffmpeg
        .input(in_filename)
        .output('pipe:', format='rawvideo', pix_fmt='rgb24', vframes=1)
        .run_async(pipe_stdout=True)
    )

    while True:
        in_bytes = process.stdout.read(width * height * 3)

        if not in_bytes:
            break

        in_frame = (
            np
            .frombuffer(in_bytes, np.uint8)
            .reshape([height, width, 3])
        )    

        decode_pix(width, height)
        
    process.stdout.flush()
    

if __name__ == "__main__":
    main()

