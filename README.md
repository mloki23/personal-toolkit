# Personal Toolkit

A collection of useful Python scripts.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### File Organizer

Organize files in a directory by extension.

```bash
python personal_toolkit_cli.py organize <directory>
```

### Password Generator

Generate a random password.

```bash
python personal_toolkit_cli.py password [--length <length>] [--no-uppercase] [--no-lowercase] [--no-digits] [--no-symbols]
```

### URL Shortener

Shorten a URL.

```bash
python personal_toolkit_cli.py shorten <url>
```

### System Info

Display system information.

```bash
python personal_toolkit_cli.py sysinfo
```

### QR Code Generator/Reader

Generate or read QR codes.

```bash
python personal_toolkit_cli.py qrcode generate <data> <output_filename>
python personal_toolkit_cli.py qrcode read <input_filename>
```

### Image Resizer/Converter

Resize or convert images.

```bash
python personal_toolkit_cli.py image resize <input_file> <output_file> --width <width> --height <height>
python personal_toolkit_cli.py image convert <input_file> <output_file> --format <format>
```

### Log File Analyzer

Analyze log files for errors or count log levels.

```bash
python personal_toolkit_cli.py log analyze <file_path> [--pattern <regex_pattern>]
python personal_toolkit_cli.py log count <file_path> [--levels <level1> <level2> ...]
```

### Network Speed Tester

Test network download and upload speeds.

```bash
python personal_toolkit_cli.py network speed
```

### File Duplicate Finder

Find duplicate files in a directory.

```bash
python personal_toolkit_cli.py duplicate <directory>
```
