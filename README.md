# TF_Speech_Recognition_MIDAS_2021
Collection of Jupyter files for MIDAS 2021 Summer Intern Project
# Tensorflow Speech Recognition Challenge
## MIDAS@IIITD Summer Internship Task (2021)


##### Applicant Details-
- Name - Ananya Komal Singh 
- Institution - Delhi Technological University (DTU)
- Department - Information Technology (IT)
- Year - 2nd Year
- Email - ananyaksingh11@gmail.com
- Date of Submission - 10/4/2021
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

######  SCORE - PUBLIC- 0.70394 , PRIVATE - 0.72183
###### *RANK* - (Not available since competition ended 3yrs ago)
###### *ENTRY* - (Not available since competition ended 3yrs ago)

&nbsp;

##### Approach -
- ##### *Feature Extraction*:
    -  Various methods of Feature Extraction form audio files are available, viz.a.viz MFCC, PLP, Log Spectrogram, LPCC,LSF, DWT and LPC...etc. However cited research papers suggested only MFCC, Log spectrogram, PLP and LPCC produce great results due to their relation to the human organs used for sound analysis and production. The results presented are achieved after MFCC and Log Spectrogram were used for Feature Extraction respectively. 
    -  According to comparisons of validation accuracy, it was observed that Log Spectrogram was producing better results than MFCC.
    -  **MFCC** -- Also known as Mel frequency cepstral coefficients, is a replication of the human hearing system intending to artificially implement the ear’s working principle with the assumption that the human ear is a reliable speaker recognizer.
    -  **Log Spectrogram** -- A spectrogram is a visual way of representing the signal strength, or “loudness”, of a signal over time at various frequencies present in a particular waveform.A spectrogram is a detailed view of audio, able to represent time, frequency, and amplitude all on one graph. A spectrogram can visually reveal broadband, electrical, or intermittent noise in audio, and can allow you to easily isolate those audio problems by sight.
- ##### *Model Architectures Explored*:
    -  Models Inlcuding RNNs such as LSTM and Convulutional Neural Networks were tested for performance with MFCC and Log SPectogram.

   
##### CODE ENVIRONMENT-
- This code is reproducible in Jupyter Notebook environment available with anaconda. Python 3 is used for the same.




