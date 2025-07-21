import re

def analyze_log_file(log_file_path, error_pattern=r'ERROR|FAIL|EXCEPTION'):
    """
    Analyzes a log file for specified error patterns and returns matching lines.
    """
    errors = []
    try:
        with open(log_file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                if re.search(error_pattern, line, re.IGNORECASE):
                    errors.append(f"Line {line_num}: {line.strip()}")
    except FileNotFoundError:
        return [f"Error: Log file not found at {log_file_path}"]
    return errors

def count_log_levels(log_file_path, levels=['INFO', 'WARNING', 'ERROR', 'DEBUG']):
    """
    Counts occurrences of specified log levels in a log file.
    """
    counts = {level: 0 for level in levels}
    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                for level in levels:
                    if re.search(r'\b' + level + r'\b', line, re.IGNORECASE):
                        counts[level] += 1
                        break # Assume one log level per line
    except FileNotFoundError:
        return {level: 0 for level in levels} # Return empty counts if file not found
    return counts