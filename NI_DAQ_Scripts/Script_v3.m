clc;
clear all;

%%
s = daq.createSession("ni");
ch = addAnalogInputChannel(s,"Dev1","ai0","Voltage")

% Define sampling rate to acquire signals
s.Rate = 1000;

% Change the channel TerminalConfig property to 'SingleEnded', and view the updated configuration
s.Channels.TerminalConfig = "Differential";
s.Channels

% % Interrupt interval
s.NotifyWhenDataAvailableExceeds = 1000;


% Define interrupt event
lh = addlistener(s,'DataAvailable',@(src, event)Dump_data(src,event));

% % Define if sampling is done continously
s.IsContinuous = true;

disp('Data collection started');
startBackground(s); % Start data acq. process in background

% Wait till data acq. is over (not required in background acq. case)
% s.wait();
%%
% Terminate data acquisition
% fclose(fid);
s.stop();
delete(lh);
close all;
disp('Data collection stopped');









