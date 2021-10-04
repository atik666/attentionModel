clear;clc;

file = '1Norm'; fs= 12000; %Sampling frequency
data = load(sprintf('D:/OneDrive - ump.edu.my/Atik_Home/Writing/Encoder/Load data/%s.mat', file));

data = struct2cell(data);
data = cell2mat(data(1,1));

dir = sprintf('D:/OneDrive - ump.edu.my/Atik_Home/Writing/Encoder/Load data/%s',file);

k = 1;
for i = 1 : 50  
    y = data(k:k+599, :)';

    [wt,f] = cwt(y,'amor',fs);
    h = figure('Visible', 'off');
    t = 0:numel(y)-1;
    hp = pcolor(t,f,abs(wt));
    hp.EdgeColor = 'none';
    set(gca,'xtick',[],'ytick',[],'xticklabel',[],'yticklabel',[]);
    exportgraphics(gca, sprintf('%s/FIG%d.png', dir, i));

    img = imread(sprintf('%s/FIG%d.png', dir, i));
    im=imresize(img,[64 64]);
    imwrite(im,sprintf('%s/FIG%d.png', dir, i));
    fprintf('Image saved = %d\n', i);

    k = k+600;
end