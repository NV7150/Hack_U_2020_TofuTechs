import sys
import serial
import serial.tools.list_ports as list_ports


class SerialCommunicator:
    # ハードの都合上，open_alwaysは機能しないのでTrue推奨　絶対closeすること！
    def __init__(self, bps: int, open_always=True):
        ports = list_ports.comports()

        found = []
        for port in ports:
            # port.descriptionはうまくでない
            if type(port.manufacturer) is str and 'Arduino' in port.manufacturer:
                found.append(port)

        if len(found) <= 0:
            print('No genuine Arduino found.')
            print('Please choose and type your MCU port\'s index:')

            for i in range(len(ports)):
                print('index:' + str(i) + ' port_name:' + ports[i].device)
            print('or just type \'end\' to quit program.')

            while True:
                i = input()
                if i == 'end':
                    print('End program')
                    sys.exit(0)
                else:
                    com = int(i)
                    if com < 0 or len(ports) <= com:
                        print('Invalid port index')
                        continue
                    else:
                        found.append(ports[com])
                        break

        selected = found[0]
        if len(found) > 1:
            print('Multiple port found')
            print('Please type your MCU port index :')
            for i in range(len(found)):
                print('index:' + str(i) + ' port_name:' + found[i].device)

            while True:
                index = int(input())
                if index < 0 or len(found) <= index:
                    print('Invalid index, try again')
                    continue
                else:
                    break

            selected = found[index]

        print('Selected:' + str(selected.device))

        if not open_always:
            self.bps = bps
            self.port = selected
            self.open_always = False
        else:
            self.serial_port = serial.Serial(selected.device, bps)
            self.open_always = True

    def send_serial(self, message):
        if not self.open_always:
            with serial.Serial(self.port.device, self.bps, timeout=0.1) as serial_port:
                serial_port.write(message.encode('ASCII'))
                serial_port.flush()

        else:
            self.serial_port.write(message.encode('ASCII'))

    def read_serial(self):
        if not self.open_always:
            with serial.Serial(self.port.device, self.bps, timeout=0.1) as serial_port:
                d = serial_port.read_all()
            return d

        else:
            return self.serial_port.read_all()

    def close_serial(self):
        if self.open_always:
            self.serial_port.close()
