function [SelectedColor, numColor] = backtrack_coloring(G, m)
n=size(G,1);
c=ones(n,1);
result = checkCondition(G, c, n);
p=1;

while ~result || c(p)>m
    result = checkCondition(G, c, p);
    if ~result && c(p)<m
        c(p)=c(p)+1;
    elseif ~result && c(p)>=m
        c(p)=1;
        p=p-1;
        c(p)=c(p)+1;
    elseif result
        p=p+1;
    elseif ~result &&  m==1
        break
    elseif p==0
        break
    end
    result = checkCondition(G, c, n);
end
b=unique(c);
x=max(b);
if result && x<=m
SelectedColor=c;
numColor=x;
else 
    disp('no feasible solution')
    SelectedColor=0;
    numColor=0;
end
end