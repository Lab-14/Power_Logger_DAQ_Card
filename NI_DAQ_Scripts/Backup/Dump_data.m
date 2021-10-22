function Dump_data(src,event)
% Dump data collected by listener
data_acq = [event.Data];

% text(10,10,sprintf('RMS=%f',rms(data_acq))
dim=[0.5, 0.2, 0.1, 0.1]; %From here you can location the position of text

plot(data_acq);

str=sprintf('%.2f',rms(data_acq)); %if No floting varibale number, use %d
% annotation('textbox',dim,'String',str,'FitBoxToText','on');
hold on;
title(str)
hold off;
% fname = sprintf('./Data/Data_%s.mat',datestr(clock,30));
fname = sprintf('Data_%s.mat',datestr(clock,30));
save(fname,'data_acq');
end