# from argparse import ArgumentParser
import optparse
import mefamo

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option('-i','--input', default='0',
                        help='Video source, should be the path to a video file.')
    parser.add_option('-o','--output_path', action='store_true',
                        help='Where to Place the CSV Output')
    options, args = parser.parse_args()

    print("Starting MeFaMo")
    mediapipe_face = mefamo.Mefamo(options.input, options.output_path)
    mediapipe_face.start()