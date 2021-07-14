# Blood-def-to-FS-txt
Program to convert voxel def files for Blood to Fresh Supply's txt format

Uses settings file for blacklisting (if the voxel doesn't work in FS) or to use an alternative voxel for FS (If pivots need adjusting, uses "_FS" suffixed files instead) based on Tile ID

Usage:
Drop the .def file onto the exe and the new .txt file should be created next to the original .def. Only works 1 file at a time

Settings file format & example:

```
[BlacklistedVoxels]
Blacklist = 3436

[FSEditedVoxels]
FSEdit = 0536, 0540, 0547
```
