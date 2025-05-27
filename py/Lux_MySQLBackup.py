"""
Lux_MySQLBackup

Copyright (c) 2025 LuxCoding

This script is licensed under the MIT License.
For full details, see the LICENSE file in the repository.
"""

# Import Libs
import os
from datetime import datetime
from functions import load_settings, decrypt, encrypt_file, SQL, log_to_discord, pack_backup_to_zip, send_backup_to_discord

# Gets Current Script Path 
script_dir = os.path.dirname(__file__)
print(script_dir)
