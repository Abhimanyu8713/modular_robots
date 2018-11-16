function J = jcbn_smores
syms q1 q2 q3 q4 F
links = 5;
a = [0 0 0 0 5];
alpha = [pi/2 pi/2 0 pi/2 pi/2];
d = [0 0 5 5 0];
theta = [pi -pi/2+q1 q2 pi+q3 pi/2+q4];
F = fk_two(links,a,alpha,d,theta)
Ft = F(1:3,4)
Q = [q1 q2 q3 q4]
for j = 1:1:3
    for i = 1:1:4
        J(j,i) = diff(Ft(j),Q(i))
        J = vpa(J,3)
    end
end
