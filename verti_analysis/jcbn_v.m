function J = jcbn_v
syms q1 q2 q3 q4 F
links = 3;
a = [42 0 42]; %length from the centre to the end-face of a modbot
alpha = [0 pi/2 0];
d = [0 0 0];
theta = [0 q1 q2]; % motor angles
F = fk_two(links,a,alpha,d,theta)
Ft = F(1:3,4)
Q = [q1 q2 q3 q4]
for j = 1:1:3
    for i = 1:1:2
        J(j,i) = diff(Ft(j),Q(i))
        J = vpa(J,3)
    end
end
