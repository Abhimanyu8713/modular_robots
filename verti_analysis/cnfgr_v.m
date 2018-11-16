function [Px Py Pz] = cnfgr_v
clear all
clc
count = 1;
links = 5;
a = [0 0 0 0 5];
alpha = [pi/2 pi/2 0 pi/2 pi/2];
d = [0 0 5 5 0];
for q1 = linspace(-pi,pi,15)
    for q2 = linspace(-pi/2,pi/2,15)
        for q3 = linspace(-pi/2,pi/2,15)
            for q4 = linspace(-pi,pi,15)
                %Q(count,1:4) = [q1 q2 q3 q4]
        theta = [pi -pi/2+q1 q2 pi+q3 pi/2+q4];
        F = fk_two(links,a,alpha,d,theta);
        Px(count) = F(1,4);
        Py(count) = F(2,4);
        Pz(count) = F(3,4);
          count = count+1;
            end
        end
    end
end
axis equal
scatter3(Px,Py,Pz)
end
        

