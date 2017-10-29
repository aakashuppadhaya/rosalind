from pydub import AudioSegment
import os
import pathlib


def generate_text_files(lines, DIR_PATH, video_number, OUTPUT_PATH):
    output_path = OUTPUT_PATH + 'text/'
    pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)
    for i in range(len(lines)):
        if(i < len(lines)-1):
            line = lines[i]
            with open('%s%d_%03d.txt' % (output_path, video_number, i+1), 'w') as f:
                f.write(line + '.')
    print('Total text files created: %d' % (len(lines)-1))


def get_audio_file(dir_path):
    for d, s, files in os.walk(dir_path):
        for f in files:
            if('.mp3' in f):
                return f
    return None


def get_time_in_milliseconds(line):
    split_1 = line.split(',')
    hr_min_sec = split_1[0]
    millisecs = int(split_1[1])

    split_2 = hr_min_sec.split(':')
    total_secs = int(split_2[0])*3600 + int(split_2[1])*60 + int(split_2[2])

    total_millisecs = total_secs*1000 + millisecs
    return total_millisecs


def generate_audio_files(DIR_PATH, video_number, OUTPUT_PATH):
    output_path = OUTPUT_PATH + 'audio/'
    pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)

    audio_file = get_audio_file(DIR_PATH)
    audio_main = AudioSegment.from_mp3(DIR_PATH + audio_file)

    with open(DIR_PATH + 'time_stamps.txt') as time_file:
        lines = time_file.readlines()
        start = 0
        for i in range(len(lines)):
            line = lines[i][:-1]
            finish = get_time_in_milliseconds(line)
            audio_part = audio_main[start: finish+1]
            print('audio : %d, length: %lf secs    %d : %d' % (i+1, (finish-start)/1000, start, finish))
            audio_part.export('%s%d_%03d.wav' % (
                output_path, video_number, i+1), format='wav')

            start = finish
    print('Total audio files created: %d' % (len(lines)))


if __name__ == '__main__':

    DATA_PATH = '/data_nas/ankit/cab_char2wav/raw_video_folders/'
    OUTPUT_PATH = '/data_nas/ankit/cab_char2wav/processed_data/'
    video_folders = {1: 'video1_President_elect_Obama_announces_economic_team/',
                     2: 'video2_fathersday/',
                     3: 'video3_obamaovaloffice/',
                     4: 'video4_obama65thday/',
                     5: 'video5_huricance/',
                     6: 'video6_us_obama/'}

    for video_number in range(5, 6):
        DIR_PATH = DATA_PATH + video_folders[video_number]
        print('video_number: %d    %s' % (
            video_number, video_folders[video_number]))
        with open(DIR_PATH + 'speech.txt', 'r') as f:
            text = f.read().replace('\n', '')
            lines = text.split('.')
            generate_text_files(lines, DIR_PATH, video_number, OUTPUT_PATH)

        generate_audio_files(DIR_PATH, video_number, OUTPUT_PATH)
        print('\n\n')

