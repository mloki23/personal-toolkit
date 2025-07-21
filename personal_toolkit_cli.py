import argparse
from personal_toolkit_file_organizer import organize_files
from personal_toolkit_password_generator import generate_password
from personal_toolkit_url_shortener import shorten_url
from personal_toolkit_system_info_checker import get_system_info
from personal_toolkit_qr_code import generate_qr_code, read_qr_code
from personal_toolkit_image_processor import resize_image, convert_image
from personal_toolkit_log_analyzer import analyze_log_file, count_log_levels
from personal_toolkit_network_tester import run_speed_test
from personal_toolkit_duplicate_finder import find_duplicate_files

def main():
    parser = argparse.ArgumentParser(description='Personal Toolkit - A collection of useful Python scripts.')
    subparsers = parser.add_subparsers(dest='command')

    # File Organizer
    parser_organize = subparsers.add_parser('organize', help='Organize files in a directory by extension.')
    parser_organize.add_argument('directory', type=str, help='The directory to organize.')

    # Password Generator
    parser_password = subparsers.add_parser('password', help='Generate a random password.')
    parser_password.add_argument('--length', type=int, default=12, help='Length of the password.')
    parser_password.add_argument('--no-uppercase', action='store_false', dest='use_uppercase', help='Do not use uppercase letters.')
    parser_password.add_argument('--no-lowercase', action='store_false', dest='use_lowercase', help='Do not use lowercase letters.')
    parser_password.add_argument('--no-digits', action='store_false', dest='use_digits', help='Do not use digits.')
    parser_password.add_argument('--no-symbols', action='store_false', dest='use_symbols', help='Do not use symbols.')

    # URL Shortener
    parser_shorten = subparsers.add_parser('shorten', help='Shorten a URL.')
    parser_shorten.add_argument('url', type=str, help='The URL to shorten.')

    # System Info
    parser_sysinfo = subparsers.add_parser('sysinfo', help='Display system information.')

    # QR Code Generator/Reader
    parser_qr = subparsers.add_parser('qrcode', help='Generate or read QR codes.')
    qr_subparsers = parser_qr.add_subparsers(dest='qr_command')
    parser_qr_gen = qr_subparsers.add_parser('generate', help='Generate a QR code.')
    parser_qr_gen.add_argument('data', type=str, help='Data to encode in the QR code.')
    parser_qr_gen.add_argument('output', type=str, help='Output filename for the QR code image.')
    parser_qr_read = qr_subparsers.add_parser('read', help='Read a QR code.')
    parser_qr_read.add_argument('input', type=str, help='Input filename of the QR code image.')

    # Image Resizer/Converter
    parser_image = subparsers.add_parser('image', help='Resize or convert images.')
    image_subparsers = parser_image.add_subparsers(dest='image_command')
    parser_image_resize = image_subparsers.add_parser('resize', help='Resize an image.')
    parser_image_resize.add_argument('input', type=str, help='Input image file.')
    parser_image_resize.add_argument('output', type=str, help='Output image file.')
    parser_image_resize.add_argument('--width', type=int, required=True, help='New width.')
    parser_image_resize.add_argument('--height', type=int, required=True, help='New height.')
    parser_image_convert = image_subparsers.add_parser('convert', help='Convert image format.')
    parser_image_convert.add_argument('input', type=str, help='Input image file.')
    parser_image_convert.add_argument('output', type=str, help='Output image file.')
    parser_image_convert.add_argument('--format', type=str, required=True, help='Output format (e.g., PNG, JPEG).')

    # Log File Analyzer
    parser_log = subparsers.add_parser('log', help='Analyze log files.')
    log_subparsers = parser_log.add_subparsers(dest='log_command')
    parser_log_analyze = log_subparsers.add_parser('analyze', help='Analyze log for errors.')
    parser_log_analyze.add_argument('file', type=str, help='Path to the log file.')
    parser_log_analyze.add_argument('--pattern', type=str, default=r'ERROR|FAIL|EXCEPTION', help='Regex pattern to search for.')
    parser_log_count = log_subparsers.add_parser('count', help='Count log levels.')
    parser_log_count.add_argument('file', type=str, help='Path to the log file.')
    parser_log_count.add_argument('--levels', nargs='+', default=['INFO', 'WARNING', 'ERROR', 'DEBUG'], help='Log levels to count.')

    # Network Speed Tester
    parser_network = subparsers.add_parser('network', help='Test network speed.')
    parser_network.add_argument('test', choices=['speed'], help='Type of test to run.')

    # File Duplicate Finder
    parser_duplicate = subparsers.add_parser('duplicate', help='Find duplicate files.')
    parser_duplicate.add_argument('directory', type=str, help='Directory to search for duplicates.')

    args = parser.parse_args()

    if args.command == 'organize':
        organize_files(args.directory)
        print(f"Files in '{args.directory}' have been organized.")
    elif args.command == 'password':
        password = generate_password(args.length, args.use_uppercase, args.use_lowercase, args.use_digits, args.use_symbols)
        print(f"Generated password: {password}")
    elif args.command == 'shorten':
        short_url = shorten_url(args.url)
        print(f"Shortened URL: {short_url}")
    elif args.command == 'sysinfo':
        info = get_system_info()
        for key, value in info.items():
            print(f"{key}: {value}")
    elif args.command == 'qrcode':
        if args.qr_command == 'generate':
            generate_qr_code(args.data, args.output)
            print(f"QR code generated and saved to {args.output}")
        elif args.qr_command == 'read':
            decoded_data = read_qr_code(args.input)
            if decoded_data:
                print(f"Decoded QR code data: {decoded_data}")
            else:
                print("Could not read QR code.")
    elif args.command == 'image':
        if args.image_command == 'resize':
            resize_image(args.input, args.output, args.width, args.height)
            print(f"Image resized and saved to {args.output}")
        elif args.image_command == 'convert':
            convert_image(args.input, args.output, args.format)
            print(f"Image converted and saved to {args.output}")
    elif args.command == 'log':
        if args.log_command == 'analyze':
            errors = analyze_log_file(args.file, args.pattern)
            if errors:
                print("Found errors:")
                for error in errors:
                    print(error)
            else:
                print("No errors found.")
        elif args.log_command == 'count':
            counts = count_log_levels(args.file, args.levels)
            print("Log level counts:")
            for level, count in counts.items():
                print(f"{level}: {count}")
    elif args.command == 'network':
        if args.test == 'speed':
            speeds = run_speed_test()
            print(f"Download Speed: {speeds['download_speed']:.2f} Mbps")
            print(f"Upload Speed: {speeds['upload_speed']:.2f} Mbps")
    elif args.command == 'duplicate':
        duplicates = find_duplicate_files(args.directory)
        if duplicates:
            print("Found duplicate files:")
            for file_hash, paths in duplicates.items():
                print(f"Hash: {file_hash}")
                for path in paths:
                    print(f"  - {path}")
        else:
            print("No duplicate files found.")

if __name__ == '__main__':
    main()