import BasicLEGOKibbleBalanceGUI
import wx
import Phidget
import LabJack_U6
import thread
import time
import serial

arduino = serial.Serial('COM4', 9600, timeout=0)

class LEGOKibbleBalanceBasic(BasicLEGOKibbleBalanceGUI.LEGOKibbleBalanceBasicFrame):
    numChannels = 3  # Number of Analog Input channels being used
    latestAinValues = [0] * numChannels  # Array for storing Voltages for each channel being used

    def __init__(self, parent):
        BasicLEGOKibbleBalanceGUI.LEGOKibbleBalanceBasicFrame.__init__(self, parent)
        Phidget.initialise()
        self.KiParam = 1
        self.KpParam = 0
        self.KdParam = 0
        self.phiVolt = 0
        self.integral = 0

        # Setup parameters for laser controls
        time.sleep(3)
        arduino.write('I')
        self.statusField.SetValue("Calibrate shadow sensor by pressing 'Zero'")

    def GetCoilVoltages(self):
        ''' Communicate with LabJack U6 and get the voltages across the resistor in series with each coil '''
        global numChannels, latestAinValues
        numChannels = 3  # Number of AIN channels being used
        latestAinValues = [0] * numChannels
        resolutionIndex = 1
        gainIndex = 0
        settlingFactor = 0
        differential = False
        numIterations = 1000

        d = LabJack_U6.U6()
        d.getCalibrationData()

        try:
            # Configure the IOs before the test starts

            # FIOEIOAnalog = (2 ** numChannels) - 1
            # fios = FIOEIOAnalog & 0xFF
            # eios = FIOEIOAnalog // 256

            d.getFeedback(LabJack_U6.PortDirWrite(Direction=[0, 0, 0], WriteMask=[0, 0, 15]))
            feedbackArguments = []
            feedbackArguments.append(LabJack_U6.DAC0_8(Value=125))
            feedbackArguments.append(LabJack_U6.PortStateRead())

            for i in range(numChannels):
                feedbackArguments.append(LabJack_U6.AIN24(i, resolutionIndex, gainIndex, settlingFactor, differential))

            # start = datetime.now()
            # Call Feedback 1000 (default) times

            i = 0
            for j in range(numChannels):
                latestAinValues[j] = 0
            while i < numIterations:
                results = d.getFeedback(feedbackArguments)
                for j in range(numChannels):
                    latestAinValues[j] += d.binaryToCalibratedAnalogVoltage(gainIndex, results[2 + j])
                i += 1

            for j in range(numChannels):
                latestAinValues[j] = latestAinValues[j] / float(numIterations)


        finally:
            d.close()

    def CalculateMass(self):
        ''' Calculate the objects mass and display the mass to the user '''
        # OffsetI = (float)(self.IOffsetField.GetValue())
        global latestAinValues
        currentB = latestAinValues[1] / 178.9 # -OffsetI
        # averageBL = 6.146513647#8.879173952#11.49739634#9.126187777#10.26402003#11
        # gravity = 9.8189
        # self.mass = currentA*averageBL/gravity
        # self.mass = -906*currentA - 0.141
        self.mass = 830 * currentB - 0.169  # CALIBRATION
        self.massField.SetValue(str(abs(self.mass)))
        self.statusField.SetValue("Completed Mass Measurement")

    def PID(self):
        ''' PID control for automatically adjusting the Kibble beam '''
        self.integral = 0
        self.GoToZero()
        time.sleep(3)
        count = 0
        self.statusField.SetValue("Measuring Mass...")
        while (True):
            global latestAinValues
            self.GetCoilVoltages()
            error = self.target - latestAinValues[2]
            self.integral = self.integral + self.KiParam * error
            self.phiVolt = (self.KpParam * error + self.integral)
            Phidget.setVoltage(self.phiVolt, 1)
            print(str(self.phiVolt))
            if abs(error) < 0.001:
                count = count + 1
            else:
                count = 0
            if count > 5:
                break
        self.GoToZero()
        self.statusField.SetValue("Mass Measured")

    def GoToZero(self):
        self.statusField.SetValue("Going to Zero")
        i = self.phiVolt
        while i != 0:
            self.phiVolt = i
            Phidget.setVoltage(self.phiVolt, 1)
            time.sleep(0.3)
            if i > 0:
                i = i - 0.05
            else:
                i = i + 0.05
            if abs(i) < 0.3:
                i = 0
        self.phiVolt = 0
        Phidget.setVoltage(0, 0)

    def measureButtonOnButtonClick(self, event):
        thread.start_new_thread(self.RunMeasurementsThread, ())

    def RunMeasurementsThread(self):
        ''' Perform a set number of mass measurements specified on the GUI. '''
        self.PID()
        self.CalculateMass()

    def zeroButtonOnButtonClick(self, event):
        ''' Obtain the voltage across the photodiode for 1 instance only. '''
        global latestAinValues
        self.GetCoilVoltages()
        self.target = latestAinValues[2]
        self.statusField.SetValue("Shadow Sensor Calibrated")
        time.sleep(2)
        self.statusField.SetValue("Load Mass Onto Platform")

# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)
# create an object of CalcFrame
frame = LEGOKibbleBalanceBasic(None)
# show the frame
frame.Show(True)
# start the applications
app.MainLoop()
