#!/usr/bin/env python3
#
# Copyright 2018 Ettus Research, a National Instruments Company
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
"""
Container for the list of image package targets, and the information about them
"""
PACKAGE_MAPPING = {
    "e310": {
        "type": "e3xx",
        "package_name": "e3xx_e310_fpga_default-g{}.zip",
        "files": ["usrp_e310_fpga.bin",
                  "usrp_e310_fpga_sg3.bin",
                  "usrp_e3xx_fpga_idle.bin",
                  "usrp_e3xx_fpga_idle_sg3.bin",
                  "usrp_e310_fpga.bit",
                  "usrp_e310_fpga_sg3.bit",
                  "usrp_e3xx_fpga_idle.bit",
                  "usrp_e3xx_fpga_idle_sg3.bit",
                  "usrp_e310_fpga.rpt",
                  "usrp_e310_fpga_sg3.rpt",
                  "usrp_e3xx_fpga_idle.rpt",
                  "usrp_e3xx_fpga_idle_sg3.rpt"]
    },
    "x300": {
        "type": "x3xx",
        "package_name": "x3xx_x300_fpga_default-g{}.zip",
        "files": ["usrp_x300_fpga_HG.bin",
                  "usrp_x300_fpga_HG.lvbitx",
                  "usrp_x300_fpga_XG.bin",
                  "usrp_x300_fpga_XG.lvbitx",
                  "usrp_x300_fpga_HG.bit",
                  "usrp_x300_fpga_HG.rpt",
                  "usrp_x300_fpga_XG.bit",
                  "usrp_x300_fpga_XG.rpt"]
    },
    "x310": {
        "type": "x3xx",
        "package_name": "x3xx_x310_fpga_default-g{}.zip",
        "files": ["usrp_x310_fpga_HG.bin",
                  "usrp_x310_fpga_HG.lvbitx",
                  "usrp_x310_fpga_XG.bin",
                  "usrp_x310_fpga_XG.lvbitx",
                  "usrp_x310_fpga_HG.bit",
                  "usrp_x310_fpga_HG.rpt",
                  "usrp_x310_fpga_XG.bit",
                  "usrp_x310_fpga_XG.rpt"]
    },
    "n310": {
        "type": "n3xx",
        "package_name": "n3xx_n310_fpga_default-g{}.zip",
        "files": ['usrp_n310_fpga_HG.bit',
                  'usrp_n310_fpga_HG.bit.md5',
                  'usrp_n310_fpga_HG.dts',
                  'usrp_n310_fpga_HG.dts.md5',
                  'usrp_n310_fpga_HG.rpt',
                  'usrp_n310_fpga_XG.bit',
                  'usrp_n310_fpga_XG.bit.md5',
                  'usrp_n310_fpga_XG.dts',
                  'usrp_n310_fpga_XG.dts.md5',
                  'usrp_n310_fpga_XG.rpt']
    },
    "n300": {
        "type": "n3xx",
        "package_name": "n3xx_n300_fpga_default-g{}.zip",
        "files": ['usrp_n300_fpga_HG.bit',
                  'usrp_n300_fpga_HG.bit.md5',
                  'usrp_n300_fpga_HG.dts',
                  'usrp_n300_fpga_HG.dts.md5',
                  'usrp_n300_fpga_HG.rpt',
                  'usrp_n300_fpga_XG.bit',
                  'usrp_n300_fpga_XG.bit.md5',
                  'usrp_n300_fpga_XG.dts',
                  'usrp_n300_fpga_XG.dts.md5',
                  'usrp_n300_fpga_XG.rpt']
    },
    "n310_aa": {
        "type": "n3xx",
        "package_name": "n3xx_n310_fpga_aurora-g{}.zip",
        "files": ['usrp_n310_fpga_AA.bit',
                  'usrp_n310_fpga_AA.bit.md5',
                  'usrp_n310_fpga_AA.dts',
                  'usrp_n310_fpga_AA.dts.md5',
                  'usrp_n310_fpga_AA.rpt',
                  'usrp_n310_fpga_HA.bit',
                  'usrp_n310_fpga_HA.bit.md5',
                  'usrp_n310_fpga_HA.dts',
                  'usrp_n310_fpga_HA.dts.md5',
                  'usrp_n310_fpga_HA.rpt',
                  'usrp_n310_fpga_XA.bit',
                  'usrp_n310_fpga_XA.bit.md5',
                  'usrp_n310_fpga_XA.dts',
                  'usrp_n310_fpga_XA.dts.md5',
                  'usrp_n310_fpga_XA.rpt']
    },
    "n310_wr": {
        "type": "n3xx",
        "package_name": "n3xx_n310_fpga_whiterabbit-g{}.zip",
        "files": ['usrp_n310_fpga_WX.bit',
                  'usrp_n310_fpga_WX.bit.md5',
                  'usrp_n310_fpga_WX.dts',
                  'usrp_n310_fpga_WX.dts.md5',
                  'usrp_n310_fpga_WX.rpt',]
    },
    "n300_wr": {
        "type": "n3xx",
        "package_name": "n3xx_n300_fpga_whiterabbit-g{}.zip",
        "files": ['usrp_n300_fpga_WX.bit',
                  'usrp_n300_fpga_WX.bit.md5',
                  'usrp_n300_fpga_WX.dts',
                  'usrp_n300_fpga_WX.dts.md5',
                  'usrp_n300_fpga_WX.rpt',]
    },
    "n310_cpld": {
        "type": "n3xx",
        "package_name": "n3xx_n310_cpld_default-g{}.zip",
        "files": ['usrp_n310_mg_cpld.svf']
    },
    'n200': {
        'type': 'usrp2',
        'package_name': 'usrp2_n200_fpga_default-g{}.zip',
        'files': ["usrp_n200_r2_fpga.bin",
                  "usrp_n200_r3_fpga.bin",
                  "usrp_n200_r4_fpga.bin",
                  "bit/usrp_n200_r3_fpga.bit",
                  "bit/usrp_n200_r4_fpga.bit"],
    },
    'n210': {
        'type': 'usrp2',
        'package_name': 'usrp2_n210_fpga_default-g{}.zip',
        'files': ["usrp_n210_r2_fpga.bin",
                  "usrp_n210_r3_fpga.bin",
                  "usrp_n210_r4_fpga.bin",
                  "bit/usrp_n210_r3_fpga.bit",
                  "bit/usrp_n210_r4_fpga.bit"],
    },
    'n200_fw': {
        'type': 'usrp2',
        'package_name': 'usrp2_n200_fw_default-g{}.zip',
        'files': ["usrp_n200_fw.bin"],
    },
    'n210_fw': {
        'type': 'usrp2',
        'package_name': 'usrp2_n210_fw_default-g{}.zip',
        'files': ["usrp_n210_fw.bin"],
    },
    'usrp2': {
        'type': 'usrp2',
        'package_name': 'usrp2_usrp2_fpga_default-g{}.zip',
        'files': ["usrp2_fpga.bin"],
    },
    'usrp2_fw': {
        'type': 'usrp2',
        'package_name': 'usrp2_usrp2_fw_default-g{}.zip',
        'files': ["usrp2_fw.bin"],
    },
    'b200': {
        'type': 'b2xx',
        'package_name': 'b2xx_b200_fpga_default-g{}.zip',
        'files': ["usrp_b200_fpga.bin"],
    },
    'b200mini': {
        'type': 'b2xx',
        'package_name': 'b2xx_b200mini_fpga_default-g{}.zip',
        'files': ["usrp_b200mini_fpga.bin"],
    },
    'b205mini': {
        'type': 'b2xx',
        'package_name': 'b2xx_b205mini_fpga_default-g{}.zip',
        'files': ["usrp_b205mini_fpga.bin"],
    },
    'b210': {
        'type': 'b2xx',
        'package_name': 'b2xx_b210_fpga_default-g{}.zip',
        'files': ["usrp_b210_fpga.bin"],
    },
    'b2xx_fw': {
        'type': 'b2xx',
        'package_name': 'b2xx_common_fw_default-g{}.zip',
        'files': ["usrp_b200_fw.hex"],
    },
    'n230': {
        'type': 'n230',
        'package_name': 'n230_n230_fpga_default-g{}.zip',
        'files': ["usrp_n230_fpga.bin",
                  "usrp_n230_fpga.bit",
                  "usrp_n230_fpga.rpt"],
    },
    'b100': {
        'type': 'usrp1',
        'package_name': 'usrp1_b100_fpga_default-g{}.zip',
        'files': ["usrp_b100_fpga_2rx.bin",
                  "usrp_b100_fpga.bin"],
    },
    'b100_fw': {
        'type': 'usrp1',
        'package_name': 'usrp1_b100_fw_default-g{}.zip',
        'files': ["usrp_b100_fw.ihx"],
    },
    'usrp1': {
        'type': 'usrp1',
        'package_name': 'usrp1_usrp1_fpga_default-g{}.zip',
        'files': ["usrp1_fpga_4rx.rbf",
                  "usrp1_fpga.rbf",
                  "usrp1_fw.ihx"],
    },
    'octoclock': {
        'type': 'octoclock',
        'package_name': 'octoclock_octoclock_fw_default-g{}.zip',
        'files': ["octoclock_bootloader.hex",
                  "octoclock_r4_fw.hex"],
    },
    'winusb_drv': {
        'type': 'usb',
        'package_name': 'usb_common_windrv_default-g{}.zip',
        'files': ["winusb_driver/",
                  "winusb_driver/erllc_uhd_b205mini.inf",
                  "winusb_driver/erllc_uhd_b100.inf",
                  "winusb_driver/erllc_uhd_b200_reinit.inf",
                  "winusb_driver/erllc_uhd_b200mini.inf",
                  "winusb_driver/erllc_uhd_b200.inf",
                  "winusb_driver/amd64/",
                  "winusb_driver/amd64/WdfCoInstaller01009.dll",
                  "winusb_driver/amd64/winusbcoinstaller2.dll",
                  "winusb_driver/x86/",
                  "winusb_driver/x86/WdfCoInstaller01009.dll",
                  "winusb_driver/x86/winusbcoinstaller2.dll",
                  "winusb_driver/erllc_uhd_usrp1.inf",
                  "winusb_driver/erllc_uhd_makecat.cdf",
                  "winusb_driver/erllc_uhd.cat"],
    },
}