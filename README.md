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
Media: MDA-S0021 4GB (?)
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
115200 Baud (?)
WIP
```

#### Network
```
Connected to cabinet router on LAN 2
FTP(?)
WIP
```
