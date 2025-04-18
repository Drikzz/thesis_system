# -*- coding: utf-8 -*-
"""Folder_setup.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uEiUIF7ZobKpCLRoHjvdXS4TVz2n0BZi

# **CLONE FIRST THE GITHUB REPOSITORY**
"""

!git clone https://github.com/Drikzz/thesis_system.git

"""# **NAVIGATE INSIDE THE REPOSITORY**"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /thesis_system/

"""# **GENERATE FOLDER STRUCTURE**"""

import os

folders = [
    "data/faces",
    "data/behavior_clips",
    "data/test_images",
    "models/YOLOv8",
    "notebooks",
    "outputs/detected_faces",
    "outputs/annotated_frames",
    "outputs/logs"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

print("Folder structure created successfully!")

"""# **CHECK LOCAL STATUS OF REPO**"""

!git status

"""## **PUSH TO GITHUB**"""

!git config --global user.email "rikzsuarez@gmail.com"
!git config --global user.name "Drikzz"

!git add .
!git commit -m "Initial push with folder structure and notebooks"
!git push https://Drikzz:<token>@github.com/Drikzz/thesis_system.git

"""# **ADD .KEEP TO EMPTY FOLDERS**"""

#add dummy file to empty folder
!touch data/faces/.gitkeep
!touch data/behavior_clips/.gitkeep
!touch data/test_images/.gitkeep
!touch notebooks/.gitkeep
!touch outputs/detected_faces/.gitkeep
!touch outputs/annotated_frames/.gitkeep
!touch outputs/logs/.gitkeep

print("Created .gitkeep files in empty directories to track them with Git.")

!ls