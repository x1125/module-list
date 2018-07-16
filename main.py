modules = list()
modules_skip = [
    'cec-gpio',
    'as3645a',
    'imx074',
    'ir-lirc-codec',
    'lirc_dev',
    'mt9t031',
    'radio-usb-si470x',
    'saa716x_ff',
    'videobuf2-core',
    'videobuf-dvb',
    'videocodec',
    'zr36016',
    'zr36050',
    'zr36060',
    'zr36067'
]
with open('/tmp/modules.list', 'rU') as f:
    for row in f:
        line = row.strip()
        if 'BUILT_MODULE_NAME' in line:
            modules.append(line.split('=')[1].replace('"', ''))

with open('/tmp/modules.list.new', 'w') as f:
    index = 0
    for module in modules:
        if any(module in s for s in modules_skip):
            continue

        f.write('BUILT_MODULE_NAME[{}]="{}"'.format(index, module))
        f.write("\n")
        f.write('BUILT_MODULE_LOCATION[{}]="media_build/v4l"'.format(index))
        f.write("\n")
        f.write('DEST_MODULE_LOCATION[{}]="/extramodules/v4l"'.format(index))
        f.write("\n")
        index += 1
