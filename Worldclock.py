#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Universal World Clock - Works on Python 2.7+ and Python 3.x
No external dependencies - Uses only standard library
Compatible with Windows, macOS, Linux, and any platform
"""

import sys
import time
import os
from datetime import datetime, timedelta

# Python 2/3 compatibility
if sys.version_info[0] >= 3:
    raw_input = input

# ANSI color codes (work on most terminals)
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BG_BLACK = '\033[40m'

# Timezone database (offset in hours from UTC)
TIMEZONES = {
    '1': ('UTC (Universal Time)', 0),
    '2': ('India (IST)', 5.5),
    '3': ('Japan (JST)', 9),
    '4': ('China (CST)', 8),
    '5': ('Singapore (SGT)', 8),
    '6': ('UAE (GST)', 4),
    '7': ('South Korea (KST)', 9),
    '8': ('Thailand (ICT)', 7),
    '9': ('Indonesia (WIB)', 7),
    '10': ('Pakistan (PKT)', 5),
    '11': ('Bangladesh (BST)', 6),
    '12': ('United Kingdom (GMT)', 0),
    '13': ('Germany (CET)', 1),
    '14': ('France (CET)', 1),
    '15': ('Italy (CET)', 1),
    '16': ('Spain (CET)', 1),
    '17': ('Russia - Moscow (MSK)', 3),
    '18': ('Turkey (TRT)', 3),
    '19': ('Greece (EET)', 2),
    '20': ('Poland (CET)', 1),
    '21': ('Netherlands (CET)', 1),
    '22': ('USA - Eastern (EST)', -5),
    '23': ('USA - Central (CST)', -6),
    '24': ('USA - Mountain (MST)', -7),
    '25': ('USA - Pacific (PST)', -8),
    '26': ('Canada - Eastern (EST)', -5),
    '27': ('Canada - Pacific (PST)', -8),
    '28': ('Brazil - Sao Paulo (BRT)', -3),
    '29': ('Mexico City (CST)', -6),
    '30': ('Argentina (ART)', -3),
    '31': ('Chile (CLT)', -3),
    '32': ('Australia - Sydney (AEDT)', 11),
    '33': ('Australia - Melbourne (AEDT)', 11),
    '34': ('Australia - Perth (AWST)', 8),
    '35': ('New Zealand (NZDT)', 13),
    '36': ('South Africa (SAST)', 2),
    '37': ('Egypt (EET)', 2),
    '38': ('Nigeria (WAT)', 1),
    '39': ('Kenya (EAT)', 3),
    '40': ('Saudi Arabia (AST)', 3),
    '41': ('Israel (IST)', 2),
}

def clear_screen():
    """Clear console screen - works on all platforms"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print application header"""
    print(Colors.BOLD + Colors.CYAN + "=" * 60 + Colors.RESET)
    print(Colors.BOLD + Colors.YELLOW + " " * 18 + "WORLD CLOCK" + Colors.RESET)
    print(Colors.BOLD + Colors.CYAN + "=" * 60 + Colors.RESET)
    print()

def display_timezone_menu():
    """Display timezone selection menu"""
    print(Colors.BOLD + Colors.MAGENTA + "Available Timezones:" + Colors.RESET)
    print(Colors.CYAN + "-" * 60 + Colors.RESET)
    
    # Display in columns for better readability
    items = sorted(TIMEZONES.items(), key=lambda x: int(x[0]))
    
    for i in range(0, len(items), 2):
        left = items[i]
        left_str = "{:2}. {}".format(left[0], left[1][0])
        
        if i + 1 < len(items):
            right = items[i + 1]
            right_str = "{:2}. {}".format(right[0], right[1][0])
            print("{:<35} {}".format(left_str, right_str))
        else:
            print(left_str)
    
    print(Colors.CYAN + "-" * 60 + Colors.RESET)
    print()

def get_utc_time():
    """Get current UTC time (Python 2 and 3 compatible)"""
    # Get current time in seconds since epoch
    current_time = time.time()
    # Convert to UTC datetime
    utc_dt = datetime.utcfromtimestamp(current_time)
    return utc_dt

def calculate_local_time(utc_time, offset_hours):
    """Calculate local time from UTC and offset"""
    # Handle fractional hours (like India's +5.5)
    total_minutes = int(offset_hours * 60)
    offset = timedelta(minutes=total_minutes)
    local_time = utc_time + offset
    return local_time

def format_time(dt):
    """Format datetime object to time string"""
    return dt.strftime("%H:%M:%S")

def format_date(dt):
    """Format datetime object to date string"""
    return dt.strftime("%A, %d %B %Y")

def format_offset(offset_hours):
    """Format timezone offset for display"""
    sign = '+' if offset_hours >= 0 else ''
    hours = int(abs(offset_hours))
    minutes = int((abs(offset_hours) - hours) * 60)
    
    if minutes > 0:
        return "UTC {}{}:{:02d}".format(sign, hours, minutes)
    else:
        return "UTC {}{}:00".format(sign, hours)

def display_clock(timezone_name, offset_hours):
    """Display live clock for selected timezone"""
    print()
    print(Colors.BOLD + Colors.GREEN + "Press Ctrl+C to return to menu" + Colors.RESET)
    print()
    
    try:
        while True:
            # Get current time
            utc_time = get_utc_time()
            local_time = calculate_local_time(utc_time, offset_hours)
            
            # Format strings
            time_str = format_time(local_time)
            date_str = format_date(local_time)
            offset_str = format_offset(offset_hours)
            
            # Clear previous line and display clock
            clear_screen()
            print_header()
            print(Colors.BOLD + Colors.YELLOW + "Timezone: " + Colors.WHITE + timezone_name + Colors.RESET)
            print(Colors.BOLD + Colors.YELLOW + "Offset:   " + Colors.WHITE + offset_str + Colors.RESET)
            print()
            print(Colors.BG_BLACK + Colors.BOLD + Colors.GREEN + " " * 60 + Colors.RESET)
            print(Colors.BG_BLACK + Colors.BOLD + Colors.GREEN + 
                  " " * 15 + time_str + " " * 15 + Colors.RESET)
            print(Colors.BG_BLACK + Colors.BOLD + Colors.CYAN + 
                  " " * 10 + date_str + " " * 10 + Colors.RESET)
            print(Colors.BG_BLACK + Colors.BOLD + Colors.GREEN + " " * 60 + Colors.RESET)
            print()
            print(Colors.GREEN + "Press Ctrl+C to return to menu" + Colors.RESET)
            
            # Sleep for 1 second
            time.sleep(1)
            
    except KeyboardInterrupt:
        # User pressed Ctrl+C
        print()
        print(Colors.YELLOW + "\nReturning to menu..." + Colors.RESET)
        time.sleep(1)

def get_user_choice():
    """Get timezone selection from user"""
    while True:
        try:
            choice = raw_input(Colors.BOLD + "Enter timezone number (or 'q' to quit): " + Colors.RESET).strip()
            
            if choice.lower() in ['q', 'quit', 'exit']:
                return None
            
            if choice in TIMEZONES:
                return choice
            else:
                print(Colors.YELLOW + "Invalid choice! Please enter a number from the list." + Colors.RESET)
                print()
        except KeyboardInterrupt:
            print()
            return None
        except EOFError:
            print()
            return None

def main():
    """Main application loop"""
    try:
        while True:
            clear_screen()
            print_header()
            display_timezone_menu()
            
            choice = get_user_choice()
            
            if choice is None:
                print()
                print(Colors.BOLD + Colors.CYAN + "=" * 60 + Colors.RESET)
                print(Colors.BOLD + Colors.YELLOW + " " * 15 + "Thank you for using World Clock!" + Colors.RESET)
                print(Colors.BOLD + Colors.CYAN + "=" * 60 + Colors.RESET)
                print()
                break
            
            timezone_name, offset_hours = TIMEZONES[choice]
            display_clock(timezone_name, offset_hours)
            
    except KeyboardInterrupt:
        print()
        print(Colors.BOLD + Colors.YELLOW + "\nGoodbye!" + Colors.RESET)
        print()
    except Exception as e:
        print(Colors.YELLOW + "\nAn error occurred: {}".format(str(e)) + Colors.RESET)
        print()

if __name__ == "__main__":
    # Check if terminal supports colors
    if os.name == 'nt':
        # Enable ANSI colors on Windows 10+
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except:
            # If it fails, disable colors
            Colors.RESET = ''
            Colors.BOLD = ''
            Colors.GREEN = ''
            Colors.CYAN = ''
            Colors.YELLOW = ''
            Colors.BLUE = ''
            Colors.MAGENTA = ''
            Colors.WHITE = ''
            Colors.BG_BLACK = ''
    
    main()