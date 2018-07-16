module-list
===========

(Badly written) tool to update the modules.list required in [tbs-linux_media-git-dkms](https://aur.archlinux.org/packages/tbs-linux_media-git-dkms/).

### Background
When using linux-lts then there are modules in v4l which can't be built because of the ABI differences.
If those modules are not required, then they can be omitted which requires re-writing the modules.list.

### How to use
1. Install via `yaourt -S tbs-linux_media-git-dkms`
2. Download [modules.list](https://aur.archlinux.org/cgit/aur.git/tree/modules.list?h=tbs-linux_media-git-dkms) from AUR to /tmp
3. Edit *modules_skip* in main.py if required
4. Run `python3 main.py` (this will create /tmp/modules.list.new)
5. Open /usr/src/tbs-linux_media-git-SOME_VERSION_HERE/dkms.conf and remove everything beneath "REMAKE_INITRD", which means:
    * all BUILT_MODULE_NAME
    * all BUILT_MODULE_LOCATION
    * all DEST_MODULE_LOCATION
6. Add new list by running `cat /tmp/modules.list.new >> /usr/src/tbs-linux_media-git-SOME_VERSION_HERE/dkms.conf`

Your build should now work. Otherwise, keep adding modules for each "Error! Build of *MODULE_NAME*.ko failed".