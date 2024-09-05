# Cell area estimation

This repository consists of a simple pipeline to estimate the area of cells in a set of images. In `ImageToMask.ipynb` we obtain masks from the cell images using a CellPose cell segmentation model. Next, we use the opencv-based `PhotoEditor.py` to manually remove masks undesired masks. The cell areas can then easily be obtained with the ImageJ software.

<img src="https://github.com/user-attachments/assets/d817b2b2-6450-495e-a9f8-40bd956f8dd3" width="500">
<img src="https://github.com/user-attachments/assets/129680c6-3ddf-49db-8bd4-e1c68a9186b3" width="500">
<img src="https://github.com/user-attachments/assets/9679851c-5480-4bfa-8585-3e9e66279e87" width="500">
<img src="https://github.com/user-attachments/assets/45f8a853-cf45-4b7d-ab4f-eaa171022f5e" width="500">
