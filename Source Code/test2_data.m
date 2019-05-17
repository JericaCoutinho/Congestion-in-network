%load the files:
util=load(['/Users/koratnilay/Study/Masters_project/pcap_traces/Imp_trace_file/Starbuck_western/CSV/util.csv']);
tpt=load(['/Users/koratnilay/Study/Masters_project/pcap_traces/Imp_trace_file/Starbuck_western/CSV/tpt.csv']);
gdpt=load(['/Users/koratnilay/Study/Masters_project/pcap_traces/Imp_trace_file/Starbuck_western/CSV/goodput.csv']);

%to plot a bar graph of utilization:
plot(util(:,2));
hold on
ylim([0,35])
xlabel('Time in Sec');
ylabel('Channel Utilization percent');
set(gca,'fontsize', 24)
hold off;
%---------------------*******--------------
%to plot utilization vs 
figure;
mapping=([util(1:474,2),tpt(1:474,2),gdpt(1:474,2)]);
temp=sortrows(mapping,1);
plot(temp(:,1),temp(:,2),'-*');
hold on;
plot(temp(:,1),temp(:,3),'-o');
legend('Throughput', 'Goodput');
xlim([0,35])
set(gca,'fontsize', 24)

