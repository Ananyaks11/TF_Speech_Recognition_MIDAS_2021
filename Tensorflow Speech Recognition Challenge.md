# Tensorflow Speech Recognition Challenge
## MIDAS@IIITD Summer Internship Task (2021)


##### Applicant Details-
Name - Ananya Komal Singh 
Institution - Delhi Technological University (DTU)
Department - Information Technology (IT)
Year - 2nd Year
Email - ananyaksingh11@gmail.com
Date of Submission - 10/4/2021
##### System Requirements-
- librosa 
- numpy
- tensorflow
- scipy
- glob
- re
- pandas 
- gc
- sklearn
- matplotlib

##### Required Details-
###### *RANK* - 
###### *SCORE* -
###### *ENTRY* - 

&nbsp;

##### Approach -
- ##### *Feature Extraction*:
    -  Various methods of Feature Extraction form audio files are available, viz.a.viz MFCC, PLP, Log Spectrogram, LPCC,LSF, DWT and LPC...etc. However cited research papers suggested only MFCC, Log spectrogram, PLP and LPCC produce great results due to their relation to the human organs used for sound analysis and production. The results presented are achieved after MFCC and Log Spectrogram were used for Feature Extraction respectively. 
    -  According to comparisons of validation accuracy, it was observed that Log Spectrogram was producing better results than MFCC.
    -  **MFCC** -- Also known as Mel frequency cepstral coefficients, is a replication of the human hearing system intending to artificially implement the ear’s working principle with the assumption that the human ear is a reliable speaker recognizer.
    -  **Log Spectrogram** -- A spectrogram is a visual way of representing the signal strength, or “loudness”, of a signal over time at various frequencies present in a particular waveform.
- ##### *Model Architectures Explored*:
   -  **LSTM** -- Long Short-Term memory models were used to obtain an accuracy of -___________ in __________ epochs. However, they seemed to be less efficient than expected since they are bulit for longer audio files. These audio files were short in time and hence they the LSTMs did not retrieve much data to remember.
   -  **CNN** -- Convolutional Neural Networks have proved themselves to be a great deal while analyzing the short audio files present in the data. They have outperformed RNNs and LSTMs in this particular case due to their efficiency. This was already predicted by cited references. The obtained accuracy was ___________ in __________epochs.
   -  **RNN** -- Recurrent Neural Networks are proven to obtain ahigh accuracy on temporal data.It is more suitable on data which requires to be put in an order like audio than CNNs. In the tests conducted by me, The accuracy obtained by RNN was _________ on ______ number of epochs respectively.
   
##### CODE ENVIRONMENT-
- This code is reproducible in Jupyter Notebook environment available with anaconda. Python 3 is used for the same.



