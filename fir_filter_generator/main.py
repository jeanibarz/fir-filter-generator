import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Generate a FIR filter')
    parser.add_argument('-sr', '--sampling_rate', type=int, default=1,
                        help='Sampling rate (in samples/sec)')
    parser.add_argument('-fl', '--filter_length', type=int, required=True,
                        help='Filter impulse response length (in samples)')
    parser.add_argument('-hpf_fc', '--hpf_fc', type=float, default=None,
                        help='High pass filter cutoff frequency (in Hz)')
    parser.add_argument('-hpf_order', '--hpf_order', type=int, default=None,
                        help='High pass filter order')
    parser.add_argument('-lpf_fc', '--lpf_fc', type=float, default=None,
                        help='Low pass filter cutoff frequency (in Hz)')
    parser.add_argument('-lpf_order', '--lpf_order', type=int, default=None,
                        help='Low pass filter order')

    args = parser.parse_args()

    hpf = False
    lpf = False

    if args.hpf_fc is not None and args.hpf_order is not None:
        if args.hpf_fc <= 0:
            raise ValueError('error: hpf_fc value must be a strict positive real value')
            exit(1)
        elif args.hpf_order <= 0:
            raise ValueError('error: hpf_order value must be a strict positive integer value')
            exit(1)
        else:
            hpf = True

    if args.lpf_fc is not None and args.lpf_order is not None:
        if args.lpf_fc <= 0:
            raise ValueError('error: lpf_fc value must be a strict positive real value')
            exit(1)
        elif args.lpf_order <= 0:
            raise ValueError('error: lpf_order value must be a strict positive integer value')
            exit(1)
        else:
            lpf = True

    if not hpf and not lpf:
        raise ValueError('error: you must specify\n'
                         '1- hpf_fc and hpf_order to generate an highpass filter,\n'
                         '2- lpf_fc and lpf_order to generate a lowpass filter,\n'
                         'or both to generate a bandpass filter')
        exit(1)
    elif hpf and lpf:
        print('Generating bandpass filter with the following characteristics:')
        print('\tSampling rate: {}'.format(args.sampling_rate))
        print('\tFilter length: {}'.format(args.filter_length))
        print('\tHPF fc: {}'.format(args.hpf_fc))
        print('\tHPF order: {}'.format(args.hpf_order))
        print('\tLPF fc: {}'.format(args.lpf_fc))
        print('\tLPF order: {}'.format(args.lpf_order))
    elif hpf:
        assert not lpf
        print('Generating highpass filter')
        print('\tSampling rate: {}'.format(args.sampling_rate))
        print('\tFilter length: {}'.format(args.filter_length))
        print('\tHPF fc: {}'.format(args.hpf_fc))
        print('\tHPF order: {}'.format(args.hpf_order))
    else:
        assert lpf and not hpf
        print('Generating lowpass filter')
        print('\tSampling rate: {}'.format(args.sampling_rate))
        print('\tFilter length: {}'.format(args.filter_length))
        print('\tLPF fc: {}'.format(args.lpf_fc))
        print('\tLPF order: {}'.format(args.lpf_order))
    print('Done')


def run_script(argv):
    """Act like a script if we were invoked like a script."""
    sys.argv = argv
    main()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
