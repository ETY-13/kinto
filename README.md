# Kinto
[![GitHub release](https://img.shields.io/github/release/rbreaves/kinto.svg)](https://github.com/rbreaves/kinto/releases)

- Fix the damn keyboard. -

When memory muscle matters (for programmers and developers).

This project is only about one thing, remapping the control key to be next to your space bar no matter what keyboard you swap into your workflow and to do it without mastering xmodmap, setxkbmap or modifying system files.

## What does this do exactly?

Remaps your keyboard to behave more like you're on a mac again and below is how the keymap will behave.

Normal apps - Alt will be Ctrl, Win/Super will be Alt, Ctrl will be Win/Super
Terminal apps (optional) - Alt will be Win/Super, Win/Super will be Alt, Ctrl will be Ctrl
Modify existing Terminal app keymap profiles (optional and with confirmation) - Copy, Paste, New Tab, etc will be remapped to user Win/Super in the physical Command (or Alt key) position.

## How to install

1. clone this repo
```
git clone https://github.com/rbreaves/kinto.git
```
2. Install python3 (If needed, most current distros have it already)

Debian or Ubuntu 16.04
```
sudo apt update
sudo apt install python3.6
```
3. Follow the prompts and the script will guide you through the rest of the setup.
```
./install.py
```

## Troubleshooting
If your keyboard is not being autodetected and configured then please run `xinput list`, if you are on linux, and copy the output into a ticket under issues. 

## Contributing

I welcome any and all contributors who want to contribute something to this project.

## License

GPL v2