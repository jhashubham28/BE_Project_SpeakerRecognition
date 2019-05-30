# Speaker-Recognition
Automatic Speaker Recognition algorithms in Python 

It contains Python programs that can be used for Speaker Recognition.SR is done by extracting MFCCs and LPCs from each speaker and then forming a speaker-specific codebook
of the same by using Vector Quantization. 
After that, the system is trained and tested for 8 different speakers.Speech Recognition is done using Python's SpeechRecognition library. 

Create virtualenv with:

	virtualenv -p python3 .env
	. .env/bin/activate

A report has been included for better understanding.