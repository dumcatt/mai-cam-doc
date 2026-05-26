# maimai Camera Serial Protocol

The *maimai* cabinet utilizes a standard RS232 serial connection to communicate between the host PC and the external camera assembly. The game acts as the master, pushing network configuration (IP/Subnet), timestamp syncs, and state triggers (Preview/Record/Stop) to the camera.

## Physical Layer & Settings

The connection is a standard RS232 serial interface.

* **Baud Rate:** 115200
* **Data Bits:** 8
* **Stop Bits:** 1
* **Parity:** None

---

## Packet Structure

All packets sent between the Host and the Camera follow a strict framed structure wrapped with a synchronizing header and a trailing checksum.

| Offset | Size | Name | Description |
| --- | --- | --- | --- |
| `0x00` | 1 | Header | Always `0xE0` |
| `0x01` | 1 | Target | Destination ID (`0x02` for Camera, `0x01` for Host) |
| `0x02` | 1 | Source | Sender ID (`0x01` for Host, `0x02` for Camera) |
| `0x03` | 1 | Length | Length of the Command + Data Payload |
| `0x04` | 1 | Command | The primary instruction byte |
| `0x05` | Variable | Data | Optional payload associated with the command |
| `0x05 + Len` | 1 | Checksum | Sum modulo 256 |

### Checksum Calculation

The checksum is an 8-bit sum (modulo 256) of all bytes starting from the **Target** byte to the end of the **Data** payload. The `0xE0` header is *not* included in the checksum calculation.

**Example Checksum Calculation (Keep-Alive):**
`E0 02 01 01 F1 F5`

* Sum = Target (`0x02`) + Source (`0x01`) + Length (`0x01`) + Command (`0xF1`) = `0xF5`

---

## Host to Camera (TX) Command Reference

These commands are issued by the Host PC (`Target: 0x02, Source: 0x01`).

| Command | Name | Payload | Description |
| --- | --- | --- | --- |
| `0xF1` | Keep-Alive | None | Standard ping sent continuously by the host. |
| `0x58` | Init Phase A | `0x00` | Handshake initialization step. |
| `0x59` | Init Phase B | `0x00` | Handshake initialization step. |
| `0x61` | Init Phase C | None | Handshake initialization step. |
| `0xB0` | Init Phase D | None | Handshake initialization step. |
| `0x11` | Set Datetime | 14 bytes (ASCII) | Sets the camera internal clock. Format: `YYYYMMDDHHMMSS`. |
| `0x80` | Set Network | 37 bytes | Pushes the static IP to the camera. Payload: `0x01` + 36 ASCII chars representing IP, Subnet, and Padding (e.g. `192168103201255255255000000000000000`). |
| `0x5A` | Preview Toggle | `0x00` or `0x02` | Toggles hardware stream state. |
| `0x21` | Sensor State | 3 bytes | Enables or disables the optical sensor. `00 00 01` (ON), `00 00 00` (OFF). |
| `0x22` | Prepare Camera | None | Wakes up and locks the video encoder pipeline. **Requires a 2.1s delay** before issuing the Start Record command. |
| `0x20` | Start Record | None | Initiates saving video to the buffer. |
| `0x35` | Set Filename | 32 bytes (ASCII) | Sets the target output filename. Must be exactly 32 bytes, padded with `\x00` (null terminators). |
| `0x25` | Commit File | None | Stops recording and commits the video file to disk/network. |

---

## Camera to Host (RX) Command Reference

These commands are issued by the Camera (`Target: 0x01, Source: 0x02`).

| Command | Name | Payload | Description |
| --- | --- | --- | --- |
| `0x01` | ACK (Acknowledge) | 2 bytes | Acknowledges a host command. Byte 1 is the echoed Host Command (e.g., `0x22`). Byte 2 is the status code (usually `0x01` for success). |
| `0x20` | Camera Status | Variable | General broadcast of status/keep-alive from the camera. |
| `0x28` | Firmware/Model | Variable | Returns hardware metrics and serial string details (e.g., `15222...VCB1001...`). |

---

## Standard Sequences

### 1. Boot / Initialization

Upon game boot, the host establishes connection and synchronizes the camera's internal state.

1. `0x58` (Init A)
2. `0x59` (Init B)
3. `0x80` (Push Network IP Configuration)
4. `0x11` (Sync System Datetime)
5. `0x61` (Init C)
6. `0xB0` (Init D)

### 2. Start Recording

Because hardware video encoders require spin-up time, the camera must be prepped before recording actually begins. Failing to wait will result in dropped commands.

1. Host sends `0x22` (Prepare Camera).
2. Camera responds with `0x01 0x22 0x01` (ACK).
3. **Host Waits ~2000ms.**
4. Host sends `0x20` (Start Record).
5. Camera responds with `0x01 0x20 0x01` (ACK).

### 3. Stop & Commit Recording

When a track finishes, the game dumps the video to a temporary file (`nowrec.mp4`). If the user agrees to upload/save it at the results screen, it is renamed and committed.

1. Host sends `0x22` (Prepare Pipeline).
2. Host sends `0x35` + `nowrec.mp4\x00\x00...` (Set Filename).
3. Host sends `0x25` (Stop/Commit File).
4. *If user opts to save:* The game repeats steps 1-3, but sends the final filename in Step 2 (e.g., `20260526234034_1.mp4\x00\x00...`).
