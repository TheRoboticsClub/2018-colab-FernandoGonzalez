import time
import cv2
import threading
import socket
import struct
import io
from PIL import Image
import numpy as np
import math
import pickle

class accessPoint():
    def __init__(self):
        self.IpServer = '192.169.0.14'
        self.IpClient = '192.169.0.1'

        self.recvPort = 5000
        self.sendPort = 5002

        self.recvServerSocket = None
        self.recvConnection = None

        self.sendServerSocket = None
        self.sendConnection = None

        self.Initialize()

    def Initialize(self):
        self.recvServerSocket = socket.socket()
        self.recvServerSocket.bind((self.IpServer, self.recvPort))
        self.recvServerSocket.listen(0)
        self.recvConnection = self.recvServerSocket.accept()[0].makefile('rb')

        self.sendServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sendServerSocket.connect((self.IpClient, self.sendPort))

class ObjectsDetection():
    def __init__(self):

        self.lock = threading.Lock()

        self.isSeen = False
        self.dist = None

    def set(self, seen, d):
        self.lock.acquire()
        (self.isSeen, self.dist) = (seen, d)
        self.lock.release()

    def get(self):
        self.lock.acquire()
        (seen, d) = (self.isSeen, self.dist)
        self.lock.release()
        return seen, d

class StreamServer():
    def __init__(self):
        self._rojo_bajos1 = np.array([0, 180,125])
        self._rojo_altos1 = np.array([15, 240, 255])

        self._stopCascade = cv2.CascadeClassifier('haarcascade/traffic_light.xml')
        self._stopDetection = ObjectsDetection()
        self._trafficLightDetection = ObjectsDetection()

        self._kill_event = threading.Event()
        self._frameLock = threading.Lock()
        #Initialize receiver thread
        self._recvbuf = threading.Thread(target=self.readBuf, args=(self._kill_event,))
        #Initialize sender thread
        self._sendbuf = threading.Thread(target=self.sendObjects, args=(self._kill_event,))
        self._ap = accessPoint()

        self._frame = None #Here is saved the frame captured from picam
        self._mask = None

        self._recvbuf.start()
        self._sendbuf.start()

    def readBuf(self, kill_event):
        try:
            while(not kill_event.is_set()):
                # Read the length of the image as a 32-bit unsigned int. If the
                # length is zero, quit the loop
                image_len = struct.unpack('<L', self._ap.recvConnection.read(struct.calcsize('<L')))[0]
                if not image_len:
                    break
                # Construct a stream to hold the image data and read the image
                # data from the connection
                image_stream = io.BytesIO()
                image_stream.write(self._ap.recvConnection.read(image_len))
                # Rewind the stream, open it as an image with PIL and do some
                # processing on it
                image_stream.seek(0)
                image = Image.open(image_stream).convert('RGB')
                #img = cv2.imread(image, 1)
                img = np.array(image)
                img = img[:, :, ::-1].copy()
                #self._frame = img
                self._frameLock.acquire()
                self._frame = img
                self._frameLock.release()
                #print(image)
                cv2.imshow('Image', img)
                cv2.waitKey(1)

                self._isStop()

            self._ap.recvConnection.close()
            self._ap.recvServerSocket.close()
        except KeyboardInterrupt:
            self._kill_event.set()

    def sendObjects(self, kill_event):
        try:
            while(not kill_event.is_set()):
                #Componer el array
                (stopBool, stopD) = self._stopDetection.get()
                #arr = [stopBool, stopD, 0, 0]
                dataString = str(stopBool) + str(stopD)
                #dataString = pickle.dumps(arr)
                self._ap.sendServerSocket.send(dataString)
            self._ap.sendConnection.close()
            self._ap.sendServerSocket.close()
        except KeyboardInterrupt:
            self._kill_event.set()

    def _filterImg(self, img, rb, ra):
        hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        mask = cv2.inRange(hsv, rb, ra)
        self._mask = mask
        print(mask.shape)
        moments = cv2.moments(mask)
        area = moments['m00']
        #if(area > 2000000):
        cv2.imshow('mask', mask)
        cv2.waitKey(1)

    def _isStop(self):
        '''
        Devuelve un booleano indicando si se visualiza una senal de stop
        y la distancia a la misma
        '''
        self._frameLock.acquire()
        img = self._frame
        self._frameLock.release()
        # convertimos la imagen a blanco y negro
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        d = None
        see = False
        # buscamos las coordenadas de la senal (si las hay) y
        # guardamos su posicion
        faces = self._stopCascade.detectMultiScale(gray, 1.3, 5)
        # Dibujamos un rectangulo en las coordenadas de cada rostro
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (125, 255, 0), 2)
            v = y + h - 5
            d = 5.5 / math.tan((8.0 * math.pi / 180) + math.atan((v - 119.865631204) / 332.262498472))
            d += 12
            see = True
        self._stopDetection.set(see, d)

if __name__ == "__main__":
    obj = StreamServer()
