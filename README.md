# mai-cam-doc
an attempt to document the maimai finale camera and how it communicates to the server and the Ringedge

# WIP

## Hardware

#### Main PCB
```
'MOVIE CAMERA CTRL BD'
Part No: 838-15222
CPU: Texas Instruments TMS320DM368ZCE
RAM: 2x Micron 2GH22 1Gb DDR2 (?)
NAND: ST M29DW128G 128Mb 
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
[E0] - New Packet
[Dest] - Destination ID (Camera)
[Source] - Source ID (PC)
[Length] - Number of bytes in payload
[Payload...] - Actual Payload
[Checksum] - Checksum of everything except for E0 (SUM(Destination, Source, Length, Payload) & 0xFF)

Wake/Ping
E0 02 01 01 F1 F5

Network
E0 02 01 26 80 01 31 39 32... 30 B0
(Translates to 192168103201 255255255000000000000000)

Status
E0 02 01 01 F0 F4
E0 02 01 01 61 65

Hardware Register (Camera position??)
E0 02 01 02 58 00 5D
E0 02 01 02 59 00 5E

Commit/Apply
E0 02 01 01 B0 B4

Start
E0 02 01 04 21 00 00 01 29

WIP
```
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
Notes: Network is only used for FTP
WIP
```
