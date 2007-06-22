from IcePAP import *
from serial import Serial
import time


class SerialIcePAP(IcePAP):
    
    def connect(self):
        if (self.Status == CStatus.Connected):
            return 0
        
        baudrate = 9600
        rtscts = 0
        xonxoff = 0
        print self.IcePAPhost
        #try:
        #self.tty = Serial(self.IcePAPhost, baudrate, rtscts =0, xonxoff=0)
	self.tty = Serial(1, baudrate, rtscts =0, xonxoff=0)
        #except:
        #    print "Exception: connection error"
        #    return -1
        self.Status = CStatus.Connected
        print "connected"
	self.buf = ''
        return 0
    
    def sendCommand(self, addr, command):
         
        try:
            cmd = ''
            if not addr is None:
                cmd = '%d:'% addr
            cmd = cmd + command 
            print command+'\r'
            self.tty.write(command+'\r\n')
            time.sleep(0.02)
            newdata = self.readline()
            newdata = self.readline()
            print newdata
            return newdata
        except:
            iex = IcePAPException(IcePAPException.Error, "Error sending command to the IcePAP(Serial)")
            raise iex
    
    def sendCommand2(self, addr, command):
                
        #try:
        cmd = ''
        if not addr is None:
        	cmd = '%d:'% addr
        cmd = cmd + command 
        print cmd
        #self.tty.write('\r\n'.join(command.split()))
    	self.tty.write(command+'\r\n')
	#newdata = self.readline()
    	#print newdata
    #self.tty.write('GO 10000\r')
    
        return 0
        #except:
        #    iex = IcePAPException(IcePAPException.Error, "Error sending command to the IcePAP(Serial)")
        #    raise iex
    
    def sendData(self, data):
        #try:
        self.tty.write(data)
        return 0
        #except:
        #    iex = IcePAPException(IcePAPException.Error, "Error sending data to the IcePAP(Serial)")
        #    raise iex
    
    def disconnect(self):
        
        if (self.Status == CStatus.Disconnected):
            return 0
        #try:
            #self.tty.__del__()
        self.Status = CStatus.Disconnected
        return 0
        #except:
        #    return -1
    
    def readline(self, maxsize=None, timeout=2):
        """maxsize is ignored, timeout in seconds is the max time that is way for a complete line"""
        tries = 0
	
        while 1:
            self.buf += self.tty.read()
            pos = self.buf.find('\n')
            if pos >= 0:
                line, self.buf = self.buf[:pos+1], self.buf[pos+1:]
                return line
            tries += 1
            #if tries * self.timeout > timeout:
	#	print 'exit bucle'
         #       break
        line, self.buf = self.buf, ''
        return line
