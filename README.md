# mai-cam-doc
an attempt to document the maimai finale camera and how it communicates to the server and the Ringedge

# WIP

## Hardware

#### Main PCB
```
'MOVIE CAMERA CTRL BD'
Part No: 838-15222
CPU: Texas Instruments TMS320DM368ZCE
RAM: 2x Micron 2GH22 64MB DDR2 (?)
NAND: ST M29DW128G 128MB
Media: MDA-S0021 16GB  (?)
OS: Embdedded Linux (?)

Interfaces:
Line out, Line in, Mic in, Ethernet, USB, RS232, SD, EXT I/O

Notes:
Videos are temporarily saved on the SD card as a .mp4 file
```

#### Display
```
'LCD MODULE 5.7 INCH TYPE'
Part No: 200-6211
Model: NEC NL6448BC18-01
Resolution: 640x480
Connection: VGA (?)
```

#### Camera Module
```
'BD CAMERA'
Part No: 601-12827-01
Model: KBCR-S01MG-HPB1022 (R 1.1)
Resolution: 1.3 MP
Output: 640x480 60FPS YUV
Controller: SONY CXD3193AR
```

## Communications

#### Serial RS232
```
Connected to COM1
During startup, the RingEdge will play a 440hz test tone to the camera on C/W
115200 Baud
```
[Serial Protocol](/docs/serial.md)


#### Boot Output
```
5_432 DDR 340 initialization passed!
Booting TI User Boot Loader
        UBL Version: 1.65f
BUILD : Mar 30 2012 : 11:49:32

        UBL Flashtype: SD/MMC
   DONE
Jumping to entry point at 0x81080000.


U-Boot 2010.12-rc2-svn (Mar 30 2012 - 11:54:09)

Cores: ARM 432 MHz
DDR:   340 MHz
I2C:   ready
DRAM:  256 MiB
MMC:   davinci: 0
*** Warning - bad CRC, using default environment

Net:   Ethernet PHY: GENERIC @ 0x01
DaVinci-EMAC
reading cramfs.bin

12869632 bytes read
reading uImage

2163988 bytes read
## Booting kernel from Legacy Image at 80700000 ...
   Image Name:   Linux-2.6.32.17-davinci1
   Created:      2012-04-19   7:35:18 UTC
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    2163924 Bytes = 2.1 MiB
   Load Address: 80008000
   Entry Point:  80008000
   Verifying Checksum ... OK
   Loading Kernel Image ... OK
OK

Starting kernel ...
```


#### Network
```
Connected to cabinet router on LAN 2
Mac: 00:D0:F1:19:04:09
IP: 192.168.103.201
FTP on Port 21
User: root
Pass: movieCam
WIP
```
