# Tesla Lock Sound Manager

## Description
A Python script designed to convert MP3 files to WAV format, suitable for use as custom lock sounds in Tesla vehicles. The script manages file sizes, ensuring compatibility with Tesla's requirements, and organizes converted and original files into appropriate directories.

## Getting Started

### Prerequisites
- Python 3.x
- pip
- ffmpeg or libav

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/windoze95/TeslaLockSoundManager.git
   cd TeslaLockSoundManager
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv teslamanager_venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     teslamanager_venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source teslamanager_venv/bin/activate
     ```

4. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Prepare Your MP3 Files**
   - Place the MP3 files you want to convert in the `mp3_in` directory.

2. **Run the Script**
   ```bash
   python TeslaLockSoundManager.py
   ```

3. **Check the Output**
   - Converted WAV files suitable for Tesla lock sounds will be in the `payload` directory.
   - Files too large for Tesla lock sounds will be moved to the `too_big` directory.
   - Original MP3 files will be archived in `archive/mp3`.

### Deactivating the Virtual Environment
When you are done, you can deactivate the virtual environment:
```bash
deactivate
```
