function Dump_data(src,event)
% Dump data collected by listener
data_acq = [event.Data];

plot(data_acq);
% hold on;

% fname = sprintf('./Data/Data_%s.mat',datestr(clock,30));
fname = sprintf('Data_%s.mat',datestr(clock,30));
save(fname,'data_acq');
end