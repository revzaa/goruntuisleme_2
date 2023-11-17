import cv2
import numpy as np

def main():
    anlik = cv2.VideoCapture(0)
    while True:
        goruntuvarsa, kesit = anlik.read()

        yenihali = cv2.cvtColor(kesit, cv2.COLOR_BGR2HSV)

        zeminkirmizi = np.array([0, 100, 100])
        üstkirmizi = np.array([10, 255, 255])

        maskeleme = cv2.inRange(yenihali, zeminkirmizi, üstkirmizi)

        
        sonuc = cv2.bitwise_and(kesit, kesit, mask=maskeleme)

        
        cv2.imshow('Original', kesit) 
        cv2.imshow('Result', sonuc)

        
        if cv2.waitKey(1) & 0xFF == ord('Q'):
            break

    
    anlik.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



