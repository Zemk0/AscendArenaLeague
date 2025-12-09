import os
import json

CONFIG_FOLDER = "configs"
WHITE_LIST = "whitelist.json"
ADMIN_LIST = "adminlist.json"
SETTINGS = "settings.json"

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_json(path, default_data):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default_data, f, indent=4)

def run_setup():
    print("🛠 Running setup...")

    create_folder(CONFIG_FOLDER)

    create_json(os.path.join(CONFIG_FOLDER, WHITE_LIST),
                {"whitelisted_users": []})

    create_json(os.path.join(CONFIG_FOLDER, ADMIN_LIST),
                {"admins": []})

    create_json(os.path.join(CONFIG_FOLDER, SETTINGS),
                {
                    "token": "",
                    "prefix": "!",
                    "activity": "IN DEVELOPMENT"
                })

    print("✔ Setup done.")
