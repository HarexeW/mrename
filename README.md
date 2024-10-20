# mRename

mRename is a batch file renaming tool designed to simplify the organization of media files for Jellyfin, Plex, and Kodi media libraries. With mRename, you can easily rename multiple files in one go, ensuring they meet the naming conventions required by your media server.

## Features

- Batch rename files to conform to Jellyfin, Plex, and Kodi naming standards.
- User-friendly command-line interface.

## Installation

To install mRename, you can download the latest version from the [Releases](https://github.com/yourusername/mRename/releases) page. Look for the `.whl` file and install it using pip:

1. Download the latest wheel file from the Releases page.
2. Install the wheel using pip:

   ```bash
   pip install path/to/mRename-latest.whl
   ```

## Usage

To use mRename, navigate to the directory containing the files you want to rename, and run the following command:

```bash
python -m mrename --y
```

The `--y` flag runs the application without any prompts, applying the renaming changes automatically.

### Example

1. Change to the directory containing the media files:

   ```bash
   cd /path/to/media/files
   ```

2. Run the mRename application:

   ```bash
   python -m mrename --y
   ```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests. Make sure to follow the coding style and guidelines outlined in the project.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the contributors and users who have helped shape mRename!
