# Cell area estimation

This repository consists of a simple pipeline to estimate the area of cells in a set of images. In `ImageToMask.ipynb` we obtain masks from the cell images using a CellPose cell segmentation model. Next, we use the opencv-based `PhotoEditor.py` to manually remove masks undesired masks. The cell areas can then easily be obtained with the ImageJ software.
