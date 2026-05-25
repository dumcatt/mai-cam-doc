import serial
import time
import argparse
import sys

def main():
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(description="Inits the maimai camera")
    parser.add_argument("-p", "--port", default="COM1", help="Serial Port (Default: COM1)")
    parser.add_argument("-b", "--baud", type=int, default=115200, help="Baud Rate (Default: 115200)")
    parser.add_argument("-s", "--standby", action="store_true", help="Send only the standby packet")
    args = parser.parse_args()

    # Define packets
    standby_packet = bytes.fromhex("E00201012226")
    sequence_packets = [
        bytes.fromhex("E0020101F1F5"), # Wake 1
        bytes.fromhex("E0020101F1F5"), # Wake 2
        # Network Config
        bytes.fromhex("E0020126800131393231363831303332303132353532353532353530303030303030303030303030B0"),
        bytes.fromhex("E0020101F1F5"), # Ping
        bytes.fromhex("E0020101F0F4"), # Ack
        bytes.fromhex("E00201016165"), # Ack
        bytes.fromhex("E002010258005D"), # Unknown Config 1
        bytes.fromhex("E002010259005E"), # Unknown Config 2
        bytes.fromhex("E0020101F1F5"), # Ping
        bytes.fromhex("E0020101B0B4"), # Ack
        bytes.fromhex("E00201025A005F"), # Unknown Config 3
        bytes.fromhex("E00201042100000129"), # Start Command
    ]

    packets_to_send = [standby_packet] if args.standby else sequence_packets

    try:
        print(f"Connecting to {args.port} at {args.baud} baud...")
        with serial.Serial(args.port, args.baud, timeout=1) as ser:
            for i, packet in enumerate(packets_to_send):
                print(f"Sending {'standby' if args.standby else 'packet'} {i+1}/{len(packets_to_send)}: {packet.hex().upper()}")
                ser.write(packet)
                time.sleep(0.2)
        
        print("Transmission complete.")

    except serial.SerialException as e:
        print(f"Error: Could not open serial port {args.port}. {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nTransmission interrupted.")
        sys.exit(0)

if __name__ == "__main__":
    main()