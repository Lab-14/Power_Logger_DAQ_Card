clear all
close all
clc

% % Print list of NI devices connected to the computer
% d1 = daqlist("ni")

% deviceInfo = d1{1, "DeviceInfo"}

%% Create a DataAcquisition Object.
d = daq("ni")

% Add an analog input channel, and view the DataAcquisition channel list:
addinput(d,"Dev1","ai0","Voltage")
% d.Channels

%%
% Define sampling rate to acquire signals
d.Rate = 1000;

% Time to capture the waveform
% t_capture = 20;

% Change the channel TerminalConfig property to 'SingleEnded', and view the updated configuration
d.Channels.TerminalConfig = "Differential";
% d.Channels
% d

% disp('Data collection started..\n')
% 
% % Acquire the data and assign it to the variable data, and plot the results.
% [data,timeStamp,triggerTime] = read(d,seconds(t_capture),"OutputFormat","Matrix");
% 
% disp('Data collection completed..\n')
% 
% plot(timeStamp,data)

% Set the callback function property to use your function.
d.ScansAvailableFcn = @plotMyData;

% Start the acquisition to run for 5 seconds in the background
start(d,"Duration",5)
scanData = read(d,"all")

%%
save('EXP-1.mat','data','timeStamp');

