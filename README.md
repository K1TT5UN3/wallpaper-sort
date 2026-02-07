# Wallpaper sort
Simple python script to convert, rename and sort newly downloaded wallpapers.

Default directory is "./new/".

Change directory temporarly by adding "config" as an argument.

The script moves everything into directory it's in and converts anything in the "new" directory into PNG. If it encounters any file not convertable it skips it and leaves it in the folder. Creates "new" directory if non existent so it can be run first time without any new images for every needed directory.

For now it only converts, renames and moves file but I want to add couple additional functions to it in the future.

TODO:
- [ ] Add pernament directory change.
- [ ] Add configurable directory for images to be moved into.
- [ ] Add recognision of popular ratios and formats and scaling it up or down depending on it.
- [ ] Add multiple formats to choose from when converting.
- [ ] Add proper error or warning messages.